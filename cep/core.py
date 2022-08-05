import requests

from models import validate_cep


def search_cep(cep):
    v_cep = validate_cep(cep)
    api_url = f"http://viacep.com.br/ws/{v_cep}/json/"
    response = requests.get(api_url)
    print(response.json())



search_cep("06090027")
# 06090027 <-- Osasco/SP
# 45860000 <-- Bahia
# 01310200 <-- Random number
