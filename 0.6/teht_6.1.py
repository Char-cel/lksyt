import random
def heitä_noppaa():
 luku = random.randint(1,6)
 return luku
while True:
    luku = heitä_noppaa()
    print(luku)

    if luku == 6:
        break

