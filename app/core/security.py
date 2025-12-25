import jwt
from config import settings

PRIVATE_KEY = settings.AUTH_JWT.PRIVATE_KEY_PATH.read_text()
PUBLIC_KEY = settings.AUTH_JWT.PUBLIC_KEY_PATH.read_text()

def encode_jwt(
        payload: dict,
        private_key: str = PRIVATE_KEY,
        algorithm: str = settings.ALGORITHM
):
    encoded = jwt.encode(payload, private_key, algorithm=algorithm)
    return encoded

def decode_jwt(
        token: str | bytes,
        public_key: str = PUBLIC_KEY,
        algorithm: str = settings.ALGORITHM
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded