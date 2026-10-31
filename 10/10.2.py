class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin= ylin
        self.kerros = alin
    def kerros_ylös(self):
        self.kerros += 1
        print(f"YLÖS => {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"ALAS => {self.kerros}")

    def siirry_kerrokseen(self,kerros):
        while self.kerros < kerros and self.kerros < self.ylin:
            self.kerros_ylös()
        while self.kerros > kerros and self.kerros > self.alin:
            self.kerros_alas();

hissi = Hissi(1,10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(4)
hissi.siirry_kerrokseen(3)

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)