from dotenv import load_dotenv
from pathlib import Path
import os
from pydantic import BaseModel

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class AuthJWT(BaseModel):
    PRIVATE_KEY_PATH: Path = BASE_DIR / "app" / "certs" / "private.pem"
    PUBLIC_KEY_PATH: Path = BASE_DIR / "app" / "certs" / "public.pem"

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    AUTH_JWT = AuthJWT()

settings = Settings()