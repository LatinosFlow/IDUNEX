#!/usr/bin/env python3
"""AUD-007 guard for named-project hardcoding and active Demo canon."""
from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path


FACTORY_REL = Path("engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py")
RUNNER_REL = Path("engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py")
GATE_REL = Path("engine/IDUNEX/03_PROJECT_FACTORY/04_DELIVERY_GATES/PROJECT_DEMO_PASS_GATE.json")
READINESS_REL = Path("engine/IDUNEX/03_PROJECT_FACTORY/06_PROJECT_TEMPL_72024b88/DEMO_TEMPLATE_READINESS.md")
REGISTRY_RELS = (
    Path("engine/IDUNEX/01_CANON_REGISTRIES/MASTER_GOVERNANCE_RULE_REGISTRY.json"),
    Path("engine/IDUNEX/00_INDEX/MASTER_GOVERNANCE_MAP.json"),
)
TEXT_SUFFIXES = {".py", ".json", ".md", ".txt", ".csv", ".yml", ".yaml"}
PROTECTED_LITERAL = "Proyecto 000 Demo"
PROTECTED_NORMALIZED = "proyecto000demo"
EXTERNAL_DEMO_RULE_IDS = {"PRJ-DEMO-001", "PRJ-DEMO-GATE-001"}


def _normalize(value: str) -> str:
    return "".join(character for character in value.casefold() if character.isalnum())


def _static_string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _static_string(node.left)
        right = _static_string(node.right)
        return left + right if left is not None and right is not None else None
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        values = [_static_string(item) for item in node.elts]
        return " ".join(value for value in values if value is not None) if any(value is not None for value in values) else None
    return None


def hardcoded_named_project_branches(path: Path) -> list[dict]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    findings = []
    condition_nodes = (ast.If, ast.IfExp, ast.While, ast.Assert)
    for node in ast.walk(tree):
        expressions = []
        if isinstance(node, condition_nodes):
            expressions.append(node.test)
        elif isinstance(node, ast.comprehension):
            expressions.extend(node.ifs)
        elif isinstance(node, ast.MatchValue):
            expressions.append(node.value)
        for expression in expressions:
            for candidate in ast.walk(expression):
                static_value = _static_string(candidate)
                if static_value is not None and PROTECTED_NORMALIZED in _normalize(static_value):
                    findings.append(
                        {
                            "path": path.as_posix(),
                            "line": getattr(node, "lineno", None),
                            "condition": ast.unparse(expression),
                        }
                    )
                    break
            else:
                continue
            break
    return findings


def _classify_literal_reference(relative_path: str) -> str:
    normalized = relative_path.replace("\\", "/")
    if normalized.startswith(("governance/authority/REFERENCIA/", "docs/project-demo/")):
        return "EXTERNAL_FIXTURE_OR_AUTHORITY_INPUT"
    if normalized.startswith(("docs/", "governance/decisions/")) or normalized in {"README.md", "GOVERNANCE_STATUS.md"}:
        return "DOCUMENTARY_OR_HISTORICAL"
    if normalized.startswith((
        "engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY/",
        "engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/",
        "engine/IDUNEX/11_RELEASE_INTERNAL/",
    )):
        return "HISTORICAL_NON_AUTHORITY"
    if normalized.startswith(("tests/", "tools/audit/")):
        return "NEGATIVE_TEST_GUARD"
    return "PROHIBITED_ACTIVE"


def classify_literal_references(repo_root: Path) -> dict:
    references = []
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if PROTECTED_LITERAL not in text:
            continue
        relative = path.relative_to(repo_root).as_posix()
        references.append({"path": relative, "classification": _classify_literal_reference(relative)})
    counts = Counter(item["classification"] for item in references)
    return {"counts": dict(sorted(counts.items())), "references": references}


def _load_runner_cases(path: Path) -> list[dict]:
    spec = importlib.util.spec_from_file_location("idunex_aud007_matrix_runner", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.cases()


def _registry_findings(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    findings = []
    required_ids = set(payload.get("required_rule_ids", []))
    forbidden_required = sorted(required_ids & EXTERNAL_DEMO_RULE_IDS)
    if forbidden_required:
        findings.append({"path": path.as_posix(), "reason": "demo_rule_required_as_active", "rule_ids": forbidden_required})
    rules = payload.get("rules", [])
    external_rules = {rule.get("rule_id"): rule for rule in rules if rule.get("rule_id") in EXTERNAL_DEMO_RULE_IDS}
    for rule_id in sorted(EXTERNAL_DEMO_RULE_IDS):
        rule = external_rules.get(rule_id)
        if rule is None:
            findings.append({"path": path.as_posix(), "reason": "external_rule_missing", "rule_id": rule_id})
            continue
        if not (
            rule.get("authority_classification") == "EXTERNAL_POST_M02_PROJECT_CONTRACT"
            and rule.get("engine_runtime_active") is False
            and rule.get("active_paths") == []
            and rule.get("validator_or_factory_affected") == "NONE_ENGINE_LEVEL"
        ):
            findings.append({"path": path.as_posix(), "reason": "external_rule_still_active", "rule_id": rule_id})
    return findings


def audit_repo(repo_root: Path) -> dict:
    repo_root = repo_root.resolve()
    factory = repo_root / FACTORY_REL
    runner = repo_root / RUNNER_REL
    gate = json.loads((repo_root / GATE_REL).read_text(encoding="utf-8"))
    readiness = (repo_root / READINESS_REL).read_text(encoding="utf-8")
    branch_findings = hardcoded_named_project_branches(factory)
    reference_report = classify_literal_references(repo_root)
    prohibited_references = [
        item for item in reference_report["references"] if item["classification"] == "PROHIBITED_ACTIVE"
    ]
    runner_cases = _load_runner_cases(runner)
    runner_findings = []
    if len(runner_cases) != 30:
        runner_findings.append({"reason": "case_count", "actual": len(runner_cases), "expected": 30})
    if any("demo" in json.dumps(case, ensure_ascii=False).casefold() for case in runner_cases):
        runner_findings.append({"reason": "demo_case_present"})
    expected_levels = {"basic": 10, "intermediate": 10, "complete": 10}
    actual_levels = Counter(case.get("level") for case in runner_cases)
    if dict(actual_levels) != expected_levels:
        runner_findings.append({"reason": "level_matrix", "actual": dict(actual_levels), "expected": expected_levels})
    gate_findings = []
    if not (
        gate.get("authority_classification") == "EXTERNAL_POST_M02_PROJECT_CONTRACT"
        and gate.get("engine_runtime_active") is False
        and gate.get("applies_by_project_name") is False
        and gate.get("status") == "EXTERNAL_BLOCKED_NOT_ACTIVE"
        and gate.get("result") == "NOT_EVALUATED"
    ):
        gate_findings.append({"path": GATE_REL.as_posix(), "reason": "gate_not_external_and_inactive"})
    if not all(token in readiness for token in ("EXTERNAL_POST_M02_PROJECT_INPUT_CONTRACT", "ENGINE_LEVEL activo:** false", "BLOCKED_BY_M02_FAIL")):
        gate_findings.append({"path": READINESS_REL.as_posix(), "reason": "readiness_not_external_and_inactive"})
    registry_findings = []
    for relative in REGISTRY_RELS:
        registry_findings.extend(_registry_findings(repo_root / relative))
    failures = branch_findings + prohibited_references + runner_findings + gate_findings + registry_findings
    return {
        "audit": "AUD-007_DEMO_HARDCODING_CHECK",
        "result": "PASS" if not failures else "FAIL",
        "active_named_project_branch_count": len(branch_findings),
        "prohibited_active_literal_reference_count": len(prohibited_references),
        "literal_reference_classification": reference_report,
        "runner_case_count": len(runner_cases),
        "runner_contains_demo_case": bool(any("demo" in json.dumps(case, ensure_ascii=False).casefold() for case in runner_cases)),
        "gate_findings": gate_findings,
        "registry_findings": registry_findings,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    result = audit_repo(Path(args.repo_root))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
