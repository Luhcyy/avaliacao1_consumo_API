import requests
from config import CAMBIO_API_KEY

def obter_taxa_cambio(moeda_origem, moeda_destino):
    #Obtém a taxa de câmbio entre duas moedas.
    url = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'
    headers = {'Authorization': f'Bearer {CAMBIO_API_KEY}'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        taxas_cambio = r.json()['rates']
        if moeda_destino in taxas_cambio:
            return taxas_cambio[moeda_destino]
        else:
            print(f'Moeda de destino {moeda_destino} não disponível.')
    else:
        print('Falha ao obter taxa de câmbio.')
        return None
