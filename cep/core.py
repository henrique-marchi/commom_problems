import json
from fastapi import requests

from models import Cep

def search_cep(cep):
    cep = Cep(**locals())
    request = requests.get(f"viacep.com.br/ws/{cep}/json/")
    json = json.loads(requests.content)
    print(json)


search_cep('09360510')