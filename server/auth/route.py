from fastapi import APIRouter , HTTPException , Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .models import SignupRequest
from .hash_utils  import hash_password , verify_password
from ..config.db import users_collection

router = APIRouter(prefix="/auth",tags=["auth"])
security = HTTPBasic()

def authenticate(credientials:HTTPBasicCredentials=Depends(security)):
    user = users_collection.find_one({"username":credientials.username})
    if not user or not verify_password(credientials.password,user["password"]):
        raise HTTPException(status_code=401,detail="Invalid credentials")
    return {"username": user["username"], "role": user["role"]}


@router.post("/signup")
def signup(req:SignupRequest):
    if users_collection.find_one({"username":req.username}):
        raise HTTPException(status_code=400,detail="user already exists")
    users_collection.insert_one({
        "username":req.username,
        "password":hash_password(req.password),
        "role" : req.role
    })
    return {"messages":"users created successfully"}

@router.get("/login")
def login(user=Depends(authenticate)):
    return {"username":user ["username"],"role":user["role"]}