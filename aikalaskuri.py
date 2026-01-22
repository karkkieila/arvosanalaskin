ajat = """2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
8 - 12 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
Alle kaksi tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
12 - 15 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
Alle kaksi tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
8 - 12 tuntia
5 - 8 tuntia
5 - 8 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
Alle kaksi tuntia
Alle kaksi tuntia
2 - 5 tuntia
5 - 8 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
8 - 12 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
Alle kaksi tuntia
2 - 5 tuntia
5 - 8 tuntia
8 - 12 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
Alle kaksi tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
Alle kaksi tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
5 - 8 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
2 - 5 tuntia
Alle kaksi tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
8 - 12 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
8 - 12 tuntia
5 - 8 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
5 - 8 tuntia
2 - 5 tuntia
2 - 5 tuntia
Alle kaksi tuntia""".split("\n")

s = 0
for aika in ajat:
    if aika.startswith("Alle"):
        s += 1.5
    else:
        print(aika)
        t1,t2 = [int(x[:2]) for x in aika.split(" - ")[:2]]
        s += (t1 + t2) / 2
print(s / len(ajat))