def uprava_seznamu(list1, list2):
    """
    Funkce na upravu dvou seznamu. Funkce vraci tri seznamy.
    Jeden ktery sjednocuje dva zadane seznamy, dalsi ketry je rozdil
    prvniho od druheho a treti ktery je rozdilem druheko od prvniho
    """
    seznam_sjed = list(list1)
    seznam_roz_1_2 = list(list1)
    seznam_roz_2_1 = list(list2)

    for zvire in list2:
        if zvire not in seznam_sjed:
            seznam_sjed.append(zvire)
            
    for zvire in list2:
        if zvire in seznam_roz_1_2:
            seznam_roz_1_2.remove(zvire)

    for zvire in list1:
        if zvire in seznam_roz_2_1:
            seznam_roz_2_1.remove(zvire)

    return seznam_sjed, seznam_roz_1_2, seznam_roz_2_1


zvirata1 = ["pes", "kočka", "králík", "had", "kanec"]
zvirata2 = ["pes", "osel", "jelen", "kanec", "koroptev"]
print()
print(zvirata1)
print(zvirata2)
print()
seznam_sjed, seznam_roz_1_2, seznam_roz_2_1 = uprava_seznamu(zvirata1, zvirata2)
print("Sjednoceni:", seznam_sjed)
print("Rozdil prvni mnoziny od druhe:", seznam_roz_1_2)
print("Rozdil druhe mnoziny od prvni:", seznam_roz_2_1)
