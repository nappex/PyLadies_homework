zvirata = ["pes", "kočka", "králík", "had"]
# Uloha 5
zvirata.sort()
print(zvirata)

zvirata.insert(2, "andulka")
print(zvirata)

# Uloha 6
zvirata_klice = []
for zvire in zvirata:
    zvirata_klice.append((zvire[1:], zvire))

zvirata_klice.sort()
print(zvirata_klice)

zvirata.clear()

for key, animal in zvirata_klice:
    zvirata.append(animal)
print(zvirata)
