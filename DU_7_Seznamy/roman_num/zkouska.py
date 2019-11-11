import itertools
import time


list_of_letter = ["I", "V", "X", "L", "C", "D", "M"]
WRONG_INPUT_2 = []

for i in range(2, 8, 1):
    for tuple in itertools.product(list_of_letter, repeat=i):
        WRONG_INPUT_2.append("".join(tuple))


print(WRONG_INPUT_2)
