import random
kuutio_maara =  int(input("anna arpakuutioden lukumäärä:"))
summa = 0
for i in range(kuutio_maara):
    arpa = random.randint(1,6)
    summa = summa + arpa
print(summa)