import mysql.connector
from geopy.distance import geodesic


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345',
    autocommit=True
)

kursori = yhteys.cursor()

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentokentän ICAO-koodi: ").upper()


kursori.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (icao1,)
)
lentokenttä1 = kursori.fetchone()

kursori.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (icao2,)
)
lentokenttä2 = cursor.fetchone()

if lentokenttä1 is None or lentokenttä2 is None:
    print("Jompaakumpaa lentokenttää ei löytynyt.")
else:
    kordinaatti1 = (lentokenttä1[0], lentokenttä1[1])
    kordinaatti2 = (lentokenttä2[0], lentokenttä2[1])

    etäisyys = geodesic(kordinaatti1, kordinaatti2).kilometers

    print(f"Lentokenttien välinen etäisyys on {etäisyys:.1f} kilometriä.")

kursori.close()
yhteys.close()