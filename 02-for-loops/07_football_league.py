stadium_capacity = int(input())
count_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for every_fan in range(1, count_fans + 1):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1
percent_a = sector_a / count_fans * 100
percent_b = sector_b / count_fans * 100
percent_v = sector_v / count_fans * 100
percent_g = sector_g / count_fans * 100
total_fans = sector_a + sector_b + sector_g + sector_v
percent_all = total_fans / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_all:.2f}%")