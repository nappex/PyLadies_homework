def mocniny(n):
    """
    Funkce vytvari slovnik v kterem jsou zaznamenany mocniny cisel
    od 1 do n. Funkce vraci slovnik.
    """
    mocniny = {}

    for i in range(1, n+1):
        mocniny[str(i)] = i**2
    return mocniny


def suma_keys_values(slovnik):
    """
    Funkce secte vsechny klice ve danem slovniku.
    Potom secte vsechny hodnoty v danem slovniku.
    Nakonec vrati N-tici (soucetklicu, soucethodnot)
    """
    suma_keys = 0
    suma_values = 0
    for key, value in slovnik.items():
        try:
            suma_keys += int(key)
            suma_values += int(value)
        except ValueError:
            suma_keys = 0
            suma_values = 0
            print("Jeden z klicu nebo hodnot ve slovniku neni cislo !")
            print("Zadej slovnik jehoz klice a hodnoty jsou celociselne.")
            break
    return (suma_keys, suma_values)


slovnik = mocniny(4)
print(slovnik)
print(suma_keys_values(slovnik))

slovnik = mocniny(8)
print(slovnik)
print(suma_keys_values(slovnik))

slovnik = {'1': 1, '2': "anna", '3': 9, '4': 16}
print(slovnik)
print(suma_keys_values(slovnik))

slovnik = {'1': 1, '2': 4, '3': "Ahoj", '4': 16}
print(slovnik)
print(suma_keys_values(slovnik))
