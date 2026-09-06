luvut = []
syote = input("Anna luku: ")
while syote != "":
    luvut.append(int(syote))
    luvut.sort(reverse=True)
    syote = input("Anna luku: ")
for luku in luvut [0:5]:
    print(luku)