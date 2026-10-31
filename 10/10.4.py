import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0
    def kiihdytä(self,muutos):
        self.nopeus = max(min(self.nopeus + muutos, self.huippunopeus),0)
    def kulje(self,matkustus):
        self.matka = (self.nopeus * matkustus + self.matka)

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<12} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.matka:<10}")


    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

autot = []
for i in range(1, 11):
    autot.append(Auto("ABC-" + str(i), random.randint(100, 200)))
nimi = "Suuri romuralli"
pituus = 8000
auto = autot
kilpailu = Kilpailu(nimi, pituus, auto)
kilpailutunnit = 0
while not kilpailu.kilpailu_ohi():
            kilpailu.tunti_kuluu()
            kilpailutunnit += 1
            if kilpailutunnit % 10 == 0:
                kilpailu.tulosta_tilanne()
kilpailu.tulosta_tilanne()
