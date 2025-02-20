from datetime import datetime, timedelta
import jwt
from config import JWT_SECRET_KEY, ALGORITHM

def create_access_token(data: dict, expires_delta: int = 30):
    to_encode = data.copy()
    expire = datatime.utcow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None