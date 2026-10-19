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
autot = []
for i in range(1, 11):
    autot.append(Auto("ABC-" + str(i), random.randint(100, 200)))

while not any(auto.matka >= 10000 for auto in autot):
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

print(f"{'Rekisteri':<12} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.matka:<10}")
