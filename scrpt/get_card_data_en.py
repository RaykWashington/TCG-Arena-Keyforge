import requests
import json

# Endpoint e headers
url = "https://decksofkeyforge.com/public-api/v1/cards"
headers = {
    "Api-Key": "ddf3511b-4c17-485d-bf62-eda44f13b131"
}

# Fazendo a requisição
response = requests.get(url, headers=headers)

# Verificando se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Salvando em arquivo JSON
    with open("cards.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Arquivo JSON salvo com sucesso!")
else:
    print(f"Erro na requisição: {response.status_code}")