obsah = []
odstavec = ""
with open("basnicka.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        odstavec += radek
        if radek == "\n":
            obsah.append(odstavec)
            odstavec = ""

obsah.reverse()

with open("basnicka_reverse.txt", mode="w", encoding="utf-8") as soubor:
    for odstavec in obsah:
        print(odstavec, file=soubor, end="")
