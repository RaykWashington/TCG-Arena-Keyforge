import jmespath
import json
from pathlib import Path

script_path = Path(__file__).resolve().parent
data_file = 'card_data_en.json'
formated_file = 'keyforge_card_list_en.json'

with open(script_path / data_file, encoding="utf-8") as file:
    card_data = json.load(file)

search_string = """
    [].{id : extraCardInfo.id,
    face:{
        front:{
            name: cardTitle, 
            type: cardType, 
            cost: '0', 
            image: cardTitleUrl
            }
        }, 
    name: cardTitle,
    type: cardType, 
    house: houses[0],
    cost: '0',
    expansion: expansions[0].expansion,
    rarity: expansions[0].rarity,
    isToken : token
    }""" #cria tokens

mapped = jmespath.search(search_string, card_data)
filtered = jmespath.search("[?expansion != 'CALL_OF_THE_ARCONS']", mapped)
indexed = {str(item['id']): item for item in mapped} # cria um dict usando id como chave pra cada carta (TCG-Arena exige uma id única)

print (filtered)
with open(script_path / formated_file, "w", encoding="utf-8") as file:
        json.dump(indexed, file, ensure_ascii=False, indent=4)

print("Json file created")