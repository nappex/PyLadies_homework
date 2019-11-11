def mocniny(n):
    """
    Funkce vytvari slovnik v kterem jsou zaznamenany mocniny cisel
    od 1 do n. Funkce vraci slovnik.
    """
    mocniny = {}

    for i in range(1, n+1):
        mocniny[str(i)] = i**2
    return mocniny


print(mocniny(4))
print(mocniny(8))
