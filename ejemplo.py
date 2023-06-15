import requests

URL = 'http://localhost:5000/'

data = {
    'accion': 'AMZN',
    'fecha_inicial': '2021-02-06',
    'fecha_final': '2021-02-24'
}

response = requests.post(URL, json=data)

print(response.text)