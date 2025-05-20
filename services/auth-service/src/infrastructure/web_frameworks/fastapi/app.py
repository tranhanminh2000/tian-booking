from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.web_frameworks.fastapi.routers.auth import router as auth_router

app = FastAPI(title="Auth Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
