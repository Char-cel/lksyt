class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0
    def kiihdytä(self,muutos):
        self.nopeus = max(min(self.nopeus + muutos, self.huippunopeus),0)
auto1 = Auto("ABC-123" , 142)
print(auto1.rekisteritunnus)
print(auto1.huippunopeus)
print(auto1.nopeus)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(auto1.nopeus)
auto1.kiihdytä(-200)
print(auto1.nopeus)