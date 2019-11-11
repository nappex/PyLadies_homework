souradnice_hada = [(0, 0), (1, 0), (2, 0)]
souradnice_potravy = [(2, 3)]


def vytvor_pole(pocet_radku, pocet_sloupcu):
    """
    vytvori dvojrozmerne pole (matice, seznam v seznamu)
    dle zadane sirky a delky a vyplni se kazde mi sto "."
    """
    seznam_radku = []
    for y in range(pocet_radku):
        radek = []
        for x in range(pocet_sloupcu):
            radek.append(".")
        seznam_radku.append(radek)
    return seznam_radku


def tiskni_pole(pole):
    """
    funkce slouzi pouze k vytisknuti dvojrozmerneho pole
    na obrazovku
    """
    print()
    print("Hraci pole:")
    for y in range(len(pole)):
        for x in range(len(pole[0])):
            print(pole[y][x], end=" ")
        print()


def vytvor_hada(pole, souradnice_hada):
    """
    Funkce nacita souradnice bodu, ktere nasledne zapise do
    dvojrozmerneho pole. Dle zadanych souradnich zaposuje na prislusne misto
    znak "X" misto "."
    """
    for x, y in souradnice_hada:
        pole[y][x] = "X"


def vytvor_potravu(pole, souradnice_potravy):
    x, y = souradnice_potravy[0]
    pole[y][x] = "?"


def pohyb(pole, souradnice_hada):
    """
    Dle zadane svetove strany se ukladaji souradnice x a y
    "v" - vychod +1 doprava apod
    """
    while True:
        svetova_strana = input("Zadej svetovou stranu v, z, s ,j:\n")
        x, y = souradnice_hada[-1]
        print(souradnice_hada)
        if svetova_strana == "v":
            if (x+1, y) in souradnice_hada:
                print("Tam už je telo hada ! GAME OVER!")
                break
            try:
                pole[y][x+1]
                souradnice_hada.append((x+1, y))
            except IndexError:
                print("Narazil jsi ! GAME OVER !")
                break

        elif svetova_strana == "j":
            if (x, y+1) in souradnice_hada:
                raise ValueError("Tam už je telo hada ! GAME OVER!")
                break
            try:
                pole[y+1][x]
                souradnice_hada.append((x, y+1))
            except IndexError:
                print("Narazil jsi ! GAME OVER !")
                break

        elif svetova_strana == "s":
            if (x, y-1) in souradnice_hada:
                raise ValueError("Tam už je telo hada ! GAME OVER!")
                break
            elif (y-1) < 0:
                raise ValueError("Narazil jsi ! GAME OVER !")
                break
            else:
                souradnice_hada.append((x, y-1))

        elif svetova_strana == "z":
            if (x-1, y) in souradnice_hada:
                raise ValueError("Tam už je telo hada ! GAME OVER!")
                break
            elif (x-1) < 0:
                raise ValueError("Narazil jsi ! GAME OVER !")
                break
            else:
                souradnice_hada.append((x-1, y))

        x, y = souradnice_hada[0]
        pole[y][x] = "."
        del souradnice_hada[0]
        vytvor_hada(pole, souradnice_hada)
        print(souradnice_hada)
        tiskni_pole(pole)


pole = vytvor_pole(10, 10)
vytvor_hada(pole, souradnice_hada)
vytvor_potravu(pole, souradnice_potravy)
tiskni_pole(pole)

pohyb(pole, souradnice_hada)
