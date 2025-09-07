import os
from functools import lru_cache
from pydantic import BaseModel
try:
    # Load .env if present (dev/local)
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # it's okay if python-dotenv isn't installed yet in some environments
    pass

class Settings(BaseModel):
    app_name: str = "FastAPI Starter"
    env: str = os.getenv("ENV", "development")
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    reload: bool = os.getenv("RELOAD", "true").lower() == "true"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
