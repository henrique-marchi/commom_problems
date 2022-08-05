from fastapi import FastAPI

from cep.core import search_cep as search
from cep.models import Cep as Validator


app = FastAPI()


@app.get("/cep")
async def get_cep(cep: str):
    validate = Validator(cep)
    return search(cep)
