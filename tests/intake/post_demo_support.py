import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTORY_PATH = REPO_ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py"


def load_factory(module_name: str = "idunex_project_factory_post_demo"):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(module_name, FACTORY_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def control_spec() -> dict:
    return {
        "project_name": "Proyecto Control Post Auditoria",
        "owner_entity": "LatinosFlow",
        "brand_name": "LatinosFlow",
        "brand_usage_scope": "demo/internal/testing",
        "brand_usage_scope_detail": "internal validation and non-commercial controlled testing",
        "brand_rights_declaration": "owner-provided controlled validation input; not engine default",
        "project_jurisdiction": "Peru; controlled internal validation",
        "model_count": 2,
        "models": [
            {
                "name": "Valeria Rios Andrade",
                "aliases": ["Vale"],
                "pseudonym": "Vale",
                "age": 20,
                "gender": "female",
                "adult_fictional": True,
                "real_person": False,
                "identity_type": "fictional_adult_synthetic",
                "role": "presentadora creativa y comunicadora de marca",
                "style_direction": "editorial contemporaneo y profesional",
            },
            {
                "name": "Mateo Vargas Salinas",
                "aliases": ["Mateo"],
                "pseudonym": "Mateo",
                "age": 30,
                "gender": "male",
                "adult_fictional": True,
                "real_person": False,
                "identity_type": "fictional_adult_synthetic",
                "role": "creador audiovisual y comunicador de marca",
                "style_direction": "editorial audiovisual y profesional",
            },
        ],
        "modalities_required": ["image", "video", "voice_audio", "music_suno", "sound", "text_copy", "qa_agent"],
        "assets_authorized": "NO_ASSETS_SUBMITTED",
        "logo_asset_policy": "LOGO_ASSET_NOT_VERIFIED",
        "creative_legal_restrictions": ["fictional adults only", "no real identity", "no minors", "no nudity", "no explicit sex"],
        "external_validation_required": True,
        "CREATIVE_OUTPUT_CERTIFIED": False,
    }


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
