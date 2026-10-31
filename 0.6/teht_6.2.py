import random
def heitä_noppaa(tahkot):
 luku = random.randint(1,tahkot)
 return luku
maksimi = int(input("Anna luku: "))

while True:
    luku = heitä_noppaa(maksimi)
    print(luku)

    if luku == maksimi:
        break

