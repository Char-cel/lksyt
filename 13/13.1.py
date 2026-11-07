
from flask import Flask
import json

app = Flask(__name__)

@app.route("/alkuluku/<int:numero>")
def tarkista_alkuluku(numero):

    if numero < 2:
        on_alkuluku = False
    else:
        on_alkuluku = True

        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                on_alkuluku = False
                break

    tulos = {"Number": numero, "isPrime": on_alkuluku}
    return json.dumps(tulos)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
