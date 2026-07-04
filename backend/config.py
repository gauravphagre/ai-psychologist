from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from common locations.
# This makes running from different working directories more reliable.
_backend_dir = Path(__file__).resolve().parent
_project_root = _backend_dir.parent

load_dotenv(_backend_dir / ".env")
load_dotenv(_project_root / ".env")


class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Psychologist")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")


settings = Settings()