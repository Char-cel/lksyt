def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa
luvut = [1,4,7,29]
print(laske_summa(luvut))