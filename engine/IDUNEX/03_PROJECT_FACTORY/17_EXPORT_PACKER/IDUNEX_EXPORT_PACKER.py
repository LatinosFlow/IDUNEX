#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, zipfile
from pathlib import Path

PACKAGE_MANIFEST_SCHEMA_REQUIRED_KEYS = [
    "project_type", "model_count_min", "model_count_max", "project_core_required",
    "chatgpt_core_files_exact", "copilot_core_files_exact", "agent_runtime_files_max",
    "output_modalities", "source_scope", "real_output_policy"
]
CHATGPT_CORE = [
    "01_PROJECT_CONTROL_CENTER.md",
    "02_PROJECT_GOVERNANCE_LOCKS.md",
    "03_PROJECT_MULTIMODAL_CORE.md",
    "04_MODEL_DIALOGUE_PERSONA_CORE.md",
    "05_IMAGE_VIDEO_REFERENCE_CONTRACTS.md",
    "06_VOICE_AUDIO_MUSIC_SUNO_CONTRACTS.md",
    "07_WARDROBE_SCENE_OBJECT_PHYSICS.md",
    "08_QA_FAILCODES_FALLBACKS.md",
    "09_SIDECARS_EVIDENCE_TRACEABILITY.md",
    "10_VENDOR_GUIDES_AND_HANDOFFS.md",
]
COPILOT_CORE = [x.replace(".md", ".docx") for x in CHATGPT_CORE]
CONFIG_END = "CONFIG_END=IDUNEX_AGENT_CONFIG_LOCKED"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def require(condition: bool, message: str):
    if not condition:
        raise RuntimeError(message)

def text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def validate_project_structure(root: str | Path) -> dict:
    root = Path(root).resolve()
    required = [
        "PROJECT_CORE", "CHATGPT", "COPILOT",
        "PROJECT_PACKAGE_MANIFEST.txt", "PROJECT_PACKAGE_QA_REPORT.md", "PROJECT_PACKAGE_SHA256SUMS.txt"
    ]
    missing = [x for x in required if not (root / x).exists()]
    require(root.exists() and root.is_dir(), f"project_root not found: {root}")
    require(not missing, f"export blocked, missing required project artifacts: {missing}")
    return {"status": "PASS", "required": required, "missing": missing}

def validate_agent_config(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    repeated_padding = bool(re.search(r"(.)\1{80,}", t))
    require(len(t) == 8000, f"{path} must be exactly 8000 characters, got {len(t)}")
    require(t.endswith(CONFIG_END), f"{path} must end with {CONFIG_END}")
    require(not repeated_padding, f"{path} contains repeated padding-like sequence")
    require(not re.search(r"[a-záéíóúñ,;:]$", t[:-len(CONFIG_END)].rstrip(), re.I), f"{path} appears truncated mid-sentence before marker")
    return {"file": path.as_posix(), "length": len(t), "marker": CONFIG_END}

def validate_agent_packs(root: str | Path) -> dict:
    root = Path(root).resolve()
    chat = root / "CHATGPT"
    cop = root / "COPILOT"
    require(chat.exists(), "CHATGPT/ missing")
    require(cop.exists(), "COPILOT/ missing")
    chat_core = sorted([p.name for p in chat.glob("*.md") if re.match(r"^\d{2}_", p.name)])
    cop_core = sorted([p.name for p in cop.glob("*.docx") if re.match(r"^\d{2}_", p.name)])
    require(chat_core == CHATGPT_CORE, f"ChatGPT core files mismatch: {chat_core}")
    require(cop_core == COPILOT_CORE, f"Copilot core files mismatch: {cop_core}")
    for cfg in [chat / "CONFIG/PROJECT-CONFIGURACION-AGENT.txt", cop / "CONFIG/PROJECT-CONFIGURACION-AGENT.txt"]:
        require(cfg.exists(), f"agent config missing: {cfg}")
        validate_agent_config(cfg)
    for mf in [chat / "MANIFESTS/SHA256SUMS.txt", cop / "MANIFESTS/SHA256SUMS.txt"]:
        require(mf.exists(), f"agent manifest missing: {mf}")
    return {"status": "PASS", "chatgpt_core_count": len(chat_core), "copilot_core_count": len(cop_core)}

def validate_profile360_models(root: str | Path) -> dict:
    root = Path(root).resolve()
    chat_models = [p for p in (root / "CHATGPT/MODELS").glob("*.md") if "README" not in p.name]
    cop_models = [p for p in (root / "COPILOT/MODELS").glob("*.docx") if "README" not in p.name]
    require(1 <= len(chat_models) <= 10, f"CHATGPT/MODELS must contain 1 to 10 Profile360 .md files, got {len(chat_models)}")
    require(1 <= len(cop_models) <= 10, f"COPILOT/MODELS must contain 1 to 10 Profile360 .docx files, got {len(cop_models)}")
    return {"status": "PASS", "chatgpt_models": len(chat_models), "copilot_models": len(cop_models)}

def validate_project_manifest_schema(root: str | Path) -> dict:
    root = Path(root).resolve()
    manifest = root / "PROJECT_PACKAGE_MANIFEST.txt"
    require(manifest.exists(), "PROJECT_PACKAGE_MANIFEST.txt missing")
    t = text(manifest)
    missing = [k for k in PACKAGE_MANIFEST_SCHEMA_REQUIRED_KEYS if k not in t]
    require(not missing, f"project manifest lacks required productive schema keys: {missing}")
    require("TEMPLATE_ONLY" not in t or "PROJECT_LEVEL_VARIABLE" in t, "real project manifest cannot remain TEMPLATE_ONLY without project-level variable declaration")
    return {"status": "PASS", "required_keys": PACKAGE_MANIFEST_SCHEMA_REQUIRED_KEYS}

def regenerate_project_sha256sums(root: str | Path) -> dict:
    root = Path(root).resolve()
    ledgers = [
        root / "PROJECT_PACKAGE_SHA256SUMS.txt",
        root / "CHATGPT/MANIFESTS/SHA256SUMS.txt",
        root / "COPILOT/MANIFESTS/SHA256SUMS.txt",
    ]
    for ledger in ledgers:
        rows = []
        for p in sorted(root.rglob("*")):
            if not p.is_file():
                continue
            if p == ledger or p.name.endswith(".sha256"):
                continue
            rows.append(f"{sha256_file(p)}  {p.relative_to(root).as_posix()}")
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return {"status": "PASS", "ledgers_regenerated": [p.relative_to(root).as_posix() for p in ledgers]}

def replace_template_hash_ledgers(root: str | Path) -> dict:
    root = Path(root).resolve()
    replaced = []
    for ledger in [root / "PROJECT_PACKAGE_SHA256SUMS.txt", root / "CHATGPT/MANIFESTS/SHA256SUMS.txt", root / "COPILOT/MANIFESTS/SHA256SUMS.txt"]:
        if not ledger.exists():
            continue
        t = ledger.read_text(encoding="utf-8", errors="replace")
        if "TEMPLATE_HASH" in t or "hash final real" in t.lower():
            regenerate_project_sha256sums(root)
            replaced.append(ledger.relative_to(root).as_posix())
    return {"status": "PASS", "template_ledgers_replaced": replaced}

def validate_project_qa_report(root: str | Path) -> dict:
    root = Path(root).resolve()
    qa = root / "PROJECT_PACKAGE_QA_REPORT.md"
    require(qa.exists(), "PROJECT_PACKAGE_QA_REPORT.md missing")
    t = text(qa)
    require("TEMPLATE_ONLY" not in t, "PROJECT_PACKAGE_QA_REPORT.md cannot remain TEMPLATE_ONLY for real package")
    for key in ["PASS", "QA", "hash", "sidecar"]:
        require(key.lower() in t.lower(), f"PROJECT_PACKAGE_QA_REPORT.md missing {key}")
    return {"status": "PASS", "qa_report": qa.relative_to(root).as_posix()}

def build_project_package(project_root: str | Path, output_zip: str | Path) -> str:
    root = Path(project_root).resolve()
    out = Path(output_zip).resolve()
    validate_project_structure(root)
    validate_agent_packs(root)
    validate_profile360_models(root)
    validate_project_manifest_schema(root)
    replace_template_hash_ledgers(root)
    regenerate_project_sha256sums(root)
    validate_project_qa_report(root)
    require(out.name == root.name + ".zip", "output zip name must match project folder name exactly plus .zip")
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(root.parent).as_posix())
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        require(bad is None, f"zip integrity failed at {bad}")
    digest = sha256_file(out)
    companion = out.with_suffix(out.suffix + ".sha256")
    companion.write_text(f"{digest}  {out.name}\n", encoding="utf-8")
    require(companion.read_text(encoding="utf-8").strip() == f"{digest}  {out.name}", "external companion mismatch after write")
    return digest

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_root")
    ap.add_argument("output_zip")
    args = ap.parse_args()
    digest = build_project_package(args.project_root, args.output_zip)
    print(json.dumps({"status": "PASS", "sha256": digest, "zip": args.output_zip}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
