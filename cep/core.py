import requests


from models import validate_cep


def search_cep(cep: str):
    v_cep = validate_cep(cep)
    api_url = f"http://viacep.com.br/ws/{v_cep}/json/"
    response = requests.get(api_url)
    return response.json()


# search_cep("09360510")
# 06090027 <-- Osasco/SP
# 45860000 <-- Bahia
# 01310200 <-- Random number
