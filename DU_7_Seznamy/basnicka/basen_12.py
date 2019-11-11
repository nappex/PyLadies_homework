from random import randrange

obsah = []

# rozdelim basen na slova a ulozim do seznamu
with open("basnicka.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        for slovo in radek.split():
            obsah.append(slovo)
        obsah.append("\n")

# vsechna slova zamíchám v seznamu náhodným způsobem
for i, slovo in enumerate(obsah):
    if slovo[-1] == "," and len(slovo) > 1:
        obsah[i] = slovo.replace(",", "")
        obsah.insert(i+1, ",")
    if slovo[-1] == "." and len(slovo) > 1:
        obsah[i] = slovo.replace(".", "")
        obsah.insert(i+1, ".")

for i in range(len(obsah)):
    index1 = randrange(len(obsah)-4)
    index2 = randrange(len(obsah)-4)
    if obsah[index1] != "\n" and obsah[index2] != "\n":
        if obsah[index1] != "," and obsah[index2] != ",":
            if obsah[index1] != "." and obsah[index2] != ".":
                obsah[index1], obsah[index2] = obsah[index2], obsah[index1]


# prepis nove basne do souboru
with open("basnicka_reverse.txt", mode="w", encoding="utf-8") as soubor:
    for slovo in obsah:
        if slovo == "\n":
            print(slovo, file=soubor, end="")
        else:
            print(slovo, file=soubor, end=" ")
