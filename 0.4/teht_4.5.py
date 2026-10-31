yritykset = 0
onnistui = False

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        onnistui = True
        break
    else:
        print("Väärä salasana")
        yritykset = yritykset + 1

if not onnistui:
    print("Pääsy evätty")