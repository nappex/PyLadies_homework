obsah = []
with open("basnicka.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        obsah.append(radek)

obsah.reverse()
with open("basnicka_reverse.txt", mode="w", encoding="utf-8") as soubor:
    for radek in obsah:
        print(radek, file=soubor, end="")
