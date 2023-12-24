from fastapi import FastAPI,APIRouter,HTTPException
from pydantic import BaseModel
from uuid import uuid4
router = APIRouter(prefix="/ping",tags=["ping"])

class Login(BaseModel):
    username : str
    id: uuid4

data = []

async def validate_user(id: uuid4):
    user_data = next((item for item in data if item["id"] == id), None)
    return user_data

@router.post("/login")
async def post_login_medthod(item : Login):
    if not item:
        raise HTTPException(status_code=400,detail="Item not found")
    print(type(item.id))
    user = {"username": item.username,"id": str(item.id)}
    data.append(user)
    print(data)
    return {"Id_user":item.id }

@router.get("/login/{id}")
async def get_login_method(id: str):
    if len(data) == 0:
        raise HTTPException(status_code=300, detail="Login before getting data")

    user_data = await validate_user(id)
    if user_data:
        return user_data
    else:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found")