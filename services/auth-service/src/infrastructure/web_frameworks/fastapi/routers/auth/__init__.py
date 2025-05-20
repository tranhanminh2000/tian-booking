
from fastapi import APIRouter
from fastapi import APIRouter
from interface_adapters.controllers.auth import LoginController

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(request):
    return LoginController(auth_service=None)
