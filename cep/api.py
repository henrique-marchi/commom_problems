from fastapi import FastAPI

# import uvicorn

from core import search_cep as search
from models import validate_cep as validator


app = FastAPI()


@app.get("/cep")
async def get_cep(cep: str):
    validate = validator(cep)
    result = search(validate)
    return result
