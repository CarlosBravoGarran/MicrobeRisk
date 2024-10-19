from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import os

router = APIRouter(prefix="/formulario",
                   tags=["formulario"],
                   responses={404: {"message":"No encontrado"}})


# Ruta a la carpeta Frontend dentro del mismo directorio que main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Ruta base de 'routes'
PARENT_DIR = os.path.dirname(BASE_DIR)  # Un nivel arriba, donde está 'Frontend'
templates = Jinja2Templates(directory=os.path.join(PARENT_DIR, "frontend"))


@router.get("/", response_class=HTMLResponse)
async def formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request" : request})

@router.post("/resultado", response_class= HTMLResponse)
async def resultado(request: Request, numero: float = Form(...)):
    cuadrado = numero ** 2
    return templates.TemplateResponse("resultado.html", {"request": request, "numero": numero, "cuadrado": cuadrado})