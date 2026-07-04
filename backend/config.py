from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Psychologist")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")


settings = Settings()