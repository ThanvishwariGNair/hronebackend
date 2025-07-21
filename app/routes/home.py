from fastapi import APIRouter, Query, status
from app import crud, models

router = APIRouter(prefix="/home", tags=["home"])

# 
@router.post("/", status_code=status.HTTP_201_CREATED)
async def get_home():
    return {"Home": "Welcome to the HROne API!"}
