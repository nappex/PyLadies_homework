def mocniny(n):
    """
    Funkce vytvari slovnik v kterem jsou zaznamenany mocniny cisel
    od 1 do n. Funkce vraci slovnik.
    """
    mocniny = {}

    for i in range(1, n+1):
        mocniny[str(i)] = i**2
    return mocniny


def vypis_slovnik(slovnik):
    """
    Funkce zapisuje zadany slovnik po radcich.
    Ve vypisu oznacuje co je klic a co hodnota
    """
    for key, value in slovnik.items():
        print("Klic {}, hodnota {}".format(key, value))


print(mocniny(4))
slovnik = mocniny(4)
vypis_slovnik(slovnik)

print(mocniny(8))
slovnik = mocniny(8)
vypis_slovnik(slovnik)
