
import requests

api_avain = "f2b4f4324c14a97daa0c398a723af0c8"


paikkakunta = input("Anna paikkakunnan nimi: ")

try:
    osoite = "https://api.openweathermap.org/data/2.5/weather"

    parametrit = {
        "q": paikkakunta,
        "appid": api_avain,
        "units": "metric",
        "lang": "fi"
    }

    vastaus = requests.get(osoite, params=parametrit, timeout=10)


    if vastaus.status_code == 200:
        data = vastaus.json()

        saa = data["weather"][0]["description"]
        lampotila = data["main"]["temp"]

        print(f"Säätila: {saa}")
        print(f"Lämpötila: {lampotila} °C")

    else:
        print("Säätietojen hakeminen epäonnistui.")

except requests.exceptions.RequestException as e:
    print("Yhteyttä sääpalveluun ei voitu muodostaa:", e)
