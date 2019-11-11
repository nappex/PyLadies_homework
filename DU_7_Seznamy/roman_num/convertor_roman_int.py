def convert_roman_to_int(roman_num):
    """
    Function for convert roman number to int.
    """
    roman_num = roman_num.upper()
    dict_roman = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                 }

    reduce_letter = ["I", "X", "C"]
    other_letter = ["V", "L", "D"]
    bad_combination = ["IM", "ID", "IC", "IL", "XD", "XM", "IXI", "XCX", "CMC",
                       "XCL", "XCD", "XCM", "IXV", "VIX", "LXC", "IXL", "CMD",
                       "IXC", "IXM", "DCM", "IVI", "XLX", "CDC", "IXX", "IIV",
                       "IIX", "XXL", "XXC", "XCC", "CCD", "CCM", "CMM"]
    suma = 0

    if roman_num:
        # Symbol in input is not for roman number
        for letter in roman_num:
            if letter not in (reduce_letter + other_letter + ["M"]):
                raise ValueError

        # symbol of roman number can not be more than 4 in input or 4 in line
        for letter in reduce_letter:
            if roman_num.count(letter) > 4 or 4 * letter in roman_num:
                raise ValueError

        #  V, L and D can be in roman num just 1 time
        for letter in other_letter:
            if roman_num.count(letter) > 1:
                raise ValueError

        # last symbol must not be higher than first one
        if len(roman_num) > 2\
                and dict_roman[roman_num[-1]] > dict_roman[roman_num[0]]:
            raise ValueError

        for combination in bad_combination:
            if combination in roman_num:
                raise ValueError

        for i, num in enumerate(roman_num):
            next_num = roman_num[(i + 1) % len(roman_num)]
            # previous_num = roman_num[i - 1]

            if dict_roman[num] < dict_roman[next_num]\
                    and (i + 1) != len(roman_num)\
                    and num in other_letter:
                raise ValueError

            elif dict_roman[num] < dict_roman[next_num]\
                    and (i + 1) != len(roman_num)\
                    and num in reduce_letter:
                suma -= dict_roman[num]

            else:
                suma += dict_roman[num]

        return suma

    else:
        raise ValueError


if __name__ == "__main__":
    while True:
        roman_num = input("\nWrite roman number convert to int: ")
        print("   Result:", roman_num, end=" = ")
        try:
            result = convert_roman_to_int(roman_num)
            print(result)

        except ValueError:
            print("Invalid roman number !")

        quit = input("\nContinue ? [y/n]:\n")
        if quit.lower() == "n" or quit.lower() == "no":
            break
