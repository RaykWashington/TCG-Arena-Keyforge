import jmespath
import json
from pathlib import Path

script_path = Path(__file__).resolve().parent
data_file = 'card_data_pt.json'
formated_file = 'keyforge_card_list_pt.json'

with open(script_path / data_file, encoding="utf-8") as file:
    card_data = json.load(file)

search_string = """
    [].{id : houses[0].id,
    face:{
        front:{
            name: card_title, 
            type: card_type, 
            cost: '0', 
            image: houses[0].normal
            }
        }, 
    name: card_title,
    type: card_type, 
    house: houses[0].house,
    cost: '0', expansion: set,
    rarity: rarity,
    isToken : card_type == 'Token Creature' }""" #cria tokens

mapped = jmespath.search(search_string, card_data)
indexed = {str(item['id']): item for item in mapped} # cria um dict usando id como chave pra cada carta (TCG-Arena exige uma id única)
#print(indexed)

with open(script_path / formated_file, "w", encoding="utf-8") as file:
        json.dump(indexed, file, ensure_ascii=False, indent=4)

print("Arquivo JSON salvo com sucesso!")