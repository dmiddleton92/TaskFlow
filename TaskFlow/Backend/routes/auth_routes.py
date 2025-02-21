#Add all the necessary imports
from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from utils.jwt_handler import create_access_token
from utils.db import users_collection   

#Create a new instance of the CryptContext class
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


def varify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register")
def register_user(username: str, password: str):
    if users_collection.find_one({"username": username}):
        return {"error": "Username already exists"}
    hashed_password = get_password_hash(password)
    users_collection.insert_one({"username": username, "password": hashed_password})
    return {"message": "User registered successfully"}


@router.post("/login")
 