obsah = []
with open("basnicka.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        obsah.append(radek)


for i, radek in enumerate(obsah):
    seznam_slov = radek.split()
    print(seznam_slov)
    seznam_slov.reverse()
    novy_radek = " ".join(seznam_slov)
    obsah[i] = novy_radek

with open("basnicka_reverse.txt", mode="w", encoding="utf-8") as soubor:
    for radek in obsah:
        print(radek, file=soubor)
