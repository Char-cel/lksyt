Kuukaudet = ("Tammikuu","Helmikuu","Maaliskuu","Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu","Elokuu","Syyskyy","Lokakuu","Marraskuu","Joulukuu")
Talvi = (1,2,12)
Kevat = (3,4,5)
Kesa = (6,7,8)
syksy = (9,10,11)

kuukausi = int(input("Anna kuukauden numero: "))
vuodenajat = ("Talvi","Talvi","Kevät","Kevät","Kevät","Kesa","Kesa","Kesa","Syksy","Syksy","Syksy","Talvi")
print(vuodenajat[kuukausi - 1])
