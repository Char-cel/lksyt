import json
import requests


try:
    vastaus = requests.get("https://api.chucknorris.io/jokes/random")
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")