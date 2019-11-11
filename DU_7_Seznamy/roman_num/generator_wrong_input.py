import itertools
import dict_right_input


list_of_letter = ["I", "V", "X", "L", "C", "D", "M"]
WRONG_INPUT_1 = ["IXII", "VIIII", "MMQCDAV", "MCMROIX", "MIM", "CMCMIII"]
WRONG_INPUT_2 = []

for i in range(2, 8, 1):
    for tuple in itertools.permutations(list_of_letter, i):
        WRONG_INPUT_1.append("".join(tuple))

for value in dict_right_input.right_input.values():
    if value in WRONG_INPUT_1:
        WRONG_INPUT_1.remove(value)

with open("list_wrong_input_1.py", mode="w", encoding="utf-8") as file:
    file.write("wrong_input = [\n")

    for roman in WRONG_INPUT_1:
        file.write("\t\t\t\t" + "\"" + roman + "\"," + "\n")

    file.write("\t\t\t]\n")


for i in range(2, 5, 1):
    for tuple in itertools.product(list_of_letter, repeat=i):
        WRONG_INPUT_2.append("".join(tuple))

for value in dict_right_input.right_input.values():
    if value in WRONG_INPUT_2:
        WRONG_INPUT_2.remove(value)

with open("list_wrong_input_2.py", mode="w", encoding="utf-8") as file:
    file.write("wrong_input = [\n")

    for roman in WRONG_INPUT_2:
        file.write("\t\t\t\t" + "\"" + roman + "\"," + "\n")

    file.write("\t\t\t]\n")
