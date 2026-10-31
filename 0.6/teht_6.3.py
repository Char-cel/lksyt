def gallona_litroiksi(gallonat):
    return gallonat * 3.785
while True:
    gallonat = float(input("anna gallonamäärä"))

    if gallonat < 0:
     break
    litrat = gallona_litroiksi(gallonat)
    print(litrat)