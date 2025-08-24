import jmespath
import json
import requests
from pathlib import Path


url = 'https://api.cardsofkeyforge.com/cards'
language = 'pt'
script_path = Path(__file__).resolve().parent
data_file_name = f"card_data_{language}.json"

HEADERS = {
    'Accept-Language': language,
    'accept':'application/json',
    'User-Agent': 'Keyforge TCG-Arena (https://github.com/RaykWashington/TCG-Arena-Keyforge)'
}


response = requests.get(url, headers=HEADERS)
print(response.json())

if response.status_code == 200:
    data = response.json()

    # Salvando em arquivo JSON
    with open(script_path / data_file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Arquivo JSON salvo com sucesso!")
else:
    print(f'Erro na requisição: {response.status_code}')
