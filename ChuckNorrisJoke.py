import requests
import json

cnjoke = "https://api.chucknorris.io/jokes/random"
headers = {"accept": "application/json"}

randomchuck = requests.get(cnjoke, headers=headers)

joke = json.loads(randomchuck.text)
randomjoke = joke['value']

print(randomjoke)
