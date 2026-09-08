import mysql.connector

# Tietokantayhteyden muodostaminen
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
   password='12345',
   autocommit= True,


)
icao =input("anna lentoaseman koodi:")

sql = f"select name, municipality from airport where ident = '{icao}'"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()

for rivi in tulos:
   print("Lentoasema:", rivi[0])
   print("Sijaintikunta:", rivi[1])


