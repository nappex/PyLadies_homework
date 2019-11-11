from random import choice


def vytvoreni_otazek(seznam_otazek):
    """
    Funkce vytvori slovnik uzivatelem zadanych odpovedi.
    Funkce bere seznam otazek, otazky muzeme v seznamu zmenit.
    Funkce vraci slovnik kde klic je otazka a odpovedi jsou v seznamu.
    """
    seznam_odpovedi = []
    slovnik_odpovedi = {}
    for otazka in seznam_otazek:
        while True:
            odpoved = input("Zadej odpoved na otazku " + otazka + " nebo "
                            "zadej \"konec\":\n")
            if odpoved.lower().strip() != "konec":
                seznam_odpovedi.append(odpoved.lower().strip())
            else:
                break
        slovnik_odpovedi[otazka] = list(seznam_odpovedi)
        seznam_odpovedi.clear()
    return slovnik_odpovedi


SEZNAM_OTAZEK = ["Kdo ?",
                 "S kym ?",
                 "Co delali ?",
                 "Kde ?",
                 "Kdy ?",
                 "Proc ?"]

SLOVNIK = dict(vytvoreni_otazek(SEZNAM_OTAZEK))
print(SLOVNIK)
while True:
    for key in SLOVNIK:
        print(choice(SLOVNIK[key]), end=" ")
    print()

    ODPOVED = input("Pokud chces uz nechces "
                    "vypsat dalsi vetu zadej \"konec\":\n")

    if ODPOVED.lower().strip() == "konec":
        print("Ukoncuji hru !!")
        break
