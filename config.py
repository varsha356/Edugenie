import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "EduGenie")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )
    enable_local_explainer: bool = (
        os.getenv("ENABLE_LOCAL_EXPLAINER", "false").lower()
        in {"1", "true", "yes", "on"}
    )
    local_explainer_model: str = os.getenv(
        "LOCAL_EXPLAINER_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    )
    max_input_chars: int = int(
        os.getenv("MAX_INPUT_CHARS", "20000")
    )


settings = Settings()