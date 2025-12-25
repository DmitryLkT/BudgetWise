from sqlalchemy import create_engine
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

try:
    with engine.connect() as conn:
        print("Connection OK")
except Exception as e:
    print("Connection failed:", e)