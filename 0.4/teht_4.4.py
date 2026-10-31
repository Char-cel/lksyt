import random
arvaus = int(input("Anna luku: "))
arvonta = random.randint(1,10)
while arvaus != arvonta:
 arvaus = int(input("Anna luku: "))
if arvaus >= arvonta:
    print("Liian suuri arvaus")
elif arvonta <= arvonta:
        print("Liian pieni arvaus")
else:
    print("Oikein")