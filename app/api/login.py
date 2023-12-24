from fastapi import FastAPI,APIRouter,HTTPException
router = APIRouter(prefix="/ping",tags=["ping"])

@router.get("/ping")
async def get_method():
    return {"I’m alive"}