def pocet_znaku(retezec):
    """
    Funkce bere jako argument retezec.
    Spocita jednotlive pismena a vrati slovnik
    ktery ma klice jednotlive pismena z retezce
    a hodnoty jsou celkovy pocet vyskytu daneho pismena v retezci.
    """
    vysledek = {}
    for i in range(len(retezec)):
        vysledek.setdefault(retezec[i], retezec.count(retezec[i]))
    return vysledek


print(pocet_znaku("hello world"))
print(pocet_znaku("mama mele maso otakarovi"))
