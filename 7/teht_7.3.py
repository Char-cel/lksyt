lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto (syötä, hae, lopeta): ")

    if toiminto == "syötä":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "hae":
        icao = input("Anna ICAO-koodi: ")
        print(lentoasemat[icao])

    elif toiminto == "lopeta":
        break

