import requests


# from models import Cep

def search_cep(cep):
    api_url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(api_url)
    print(response.json())


search_cep(45860000)

#01310200