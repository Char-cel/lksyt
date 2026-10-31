import math

def yksikköhinta(halkaisija, hinta):
    halkaisija = halkaisija/100
    säde = halkaisija / 2
    A = math.pi * säde ** 2
    return hinta/A



halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))

yksikköhinta1 = yksikköhinta(halkaisija1, hinta1)


halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))

yksikköhinta2 = yksikköhinta(halkaisija2, hinta2)


if yksikköhinta1 < yksikköhinta2:
    print("Pizza 1 on parempi vastine rahalle")
elif   yksikköhinta1 < yksikköhinta2:
        print("Pizza 1 on parempi vastine rahalle")
else:
     print("molemmat ovat hyviä")
     