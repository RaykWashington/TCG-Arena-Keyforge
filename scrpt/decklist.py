import requests

deck_id = "28c9c440-ced1-4e6b-ad56-21f536ffbeb2"
url = f"https://www.keyforgegame.com/api/decks/{deck_id}/?links=cards"

response = requests.get(url)
data = response.json()

cardList = []

# Extrai os nomes das cartas
for id in data["data"]["_links"]["cards"]:
    for card in data["_linked"]["cards"]:
        if card["id"] == id:
            cardList.append(card["card_title"])

for card in set(cardList):
    print(str(cardList.count(card)) + " " + card)