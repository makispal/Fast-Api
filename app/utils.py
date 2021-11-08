from typing import Any
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def to_hash(password: str) -> Any:
    return pwd_context.hash(password)

def to_verify(plain_password: str, hashed_password: str) -> Any:
    print("Plain_Pass: ", plain_password)
    print("Hashed_Pass: ", hashed_password)
    return pwd_context.verify(plain_password, hashed_password)