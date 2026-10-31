def parittomat(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset


luvut = [56, 7, 21, 6]

karsittu = parittomat(luvut)

print(luvut)
print(karsittu)