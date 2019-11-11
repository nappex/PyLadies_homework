def kratke_slova(list):
    """
    Funkce hleda v seznamu sloa kratsi nez 5 pismen
    """
    vysledek = []
    for slovo in list:
        if len(slovo) < 5:
            vysledek.append(slovo)
    return vysledek


def slova_k(list):
    """
    funkce hleda v seznamu zvirata zacinajici na "k"
    """
    vysledek = []
    for slovo in list:
        if slovo[0].lower() == "k":
            vysledek.append(slovo)
    return vysledek


def findin_slovo(list):
    """
    Uzivatel zada zvire, funkce hleda je stli zadane zvire je vseznamu
    ci nikoliv
    """
    while True:
        slovo = input("Napis zvire, ktere si myslíš ze je ve seznamu:\n")
        if not 2 < len(slovo) < 15:
            print("Napsal jsi nejakou blbost zkus to znova")
        else:
            break
    for zvire in list:
        if slovo.lower() == zvire:
            return (True, slovo.lower())
    return (False, slovo.lower())


# Uloha 0
zvirata = ["pes", "kočka", "králík", "had"]

# Uloha 1
kratka_zvirata = kratke_slova(zvirata)
print(kratka_zvirata)

# Uloha 2
kratka_k = slova_k(zvirata)
print(kratka_k)

# Uloha 3
exist_zvire, slovo = findin_slovo(zvirata)
if exist_zvire:
    print("Zadane zvire", slovo, "je v seznamu.")
else:
    print("Zadane zvire", slovo, "neni v seznamu.")
