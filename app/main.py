from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .router.router import ping, login

app = FastAPI()
app.include_router(ping.router, prefix="/api")
app.include_router(login.router, prefix="/api")
