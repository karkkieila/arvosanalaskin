k = input("Kurssi: 1. OhPe, 2.OOP: ")
p = input("Prosentit (erota pilkuilla): ")
kp = int(input("Koepisteet: "))

if k == "1":
    max_pisteet = (31,26,34,38,30,22,20)
else:
    max_pisteet = (27,31,23,24,28,17,1)

kierrospisteet = [int(pist) for pist in p.split(",")]

tulos = [x[0]/100 * x[1] for x in zip(kierrospisteet,max_pisteet)]

print(tulos)
print("Yhteensä:", sum(tulos))

painotettu = sum(tulos) / sum(max_pisteet) * 50
print("Painotettu:", painotettu)

print("Tentti painotettu:", (kp/30 * 50))

yhdistetty = painotettu + (kp / 30) * 50
print("Yhdistetty:", yhdistetty)
