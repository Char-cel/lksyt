leiviskat = float(input("anna leiviskat:"))
naulaut = float(input("anna Naulat"))
luodit = float(input("anna luodit"))

yhluodit = leiviskat * 20 * 32 + naulaut * 32 + luodit
g = yhluodit * 13.3
kg = int(g//1000)
jaljellejaavatg = g % 1000

print(f"Paino on {kg}kilogrammaa ja { jaljellejaavatg:.1f} grammaa.")