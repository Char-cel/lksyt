class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdytä(self, muutos):
        self.nopeus = max(min(self.nopeus + muutos, self.huippunopeus), 0)

    def kulje(self, matkustus):
        self.matka = self.nopeus * matkustus + self.matka


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko



sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttoaine_auto = Polttomoottoriauto("ACD-123", 165, 32.3)


sahkoauto.kiihdytä(100)
polttoaine_auto.kiihdytä(80)


sahkoauto.kulje(3)
polttoaine_auto.kulje(3)


print(f"Sähköauton matkamittari: {sahkoauto.matka} km")
print(f"Polttomoottoriauton matkamittari: {polttoaine_auto.matka} km")

