
from flask import Flask
import json
import mysql.connector

app = Flask(__name__)

@app.route("/kenttä/<icao>")
def hae_kentta(icao):

    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='OMA_SALASANA',
        autocommit=True,
        use_pure=True
    )

    kursori = yhteys.cursor()

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))

    tulos = kursori.fetchone()

    yhteys.close()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }

        return json.dumps(vastaus)

    return json.dumps({"error": "Lentokenttää ei löytynyt"})

if __name__ == "__main__":
    app.run(port=3000, debug=True)

