import mysql.connector

# Tietokantayhteyden muodostaminen
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345',
    autocommit=True,

)
maakoodi = input("Anna maakoodi:")


sql = f"select type, count(*) from airport where iso_country = '{maakoodi}' group by type"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
print(tulos)

for rivi in tulos
    print(rivi[0], ":", rivi[1])



