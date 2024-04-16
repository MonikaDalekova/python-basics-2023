kind_flower = input()
count_flowers = int(input())
budget = int(input())

flower_price = 0
discount = 0

if kind_flower == "Roses":
    flower_price = 5
    if count_flowers > 80:
        discount = 0.1
elif kind_flower == "Dahlias":
    flower_price = 3.80
    if count_flowers > 90:
        discount = 0.15
elif kind_flower == "Tulips":
    flower_price = 2.80
    if count_flowers > 80:
        discount = 0.15
elif kind_flower == "Narcissus":
    flower_price = 3
    if count_flowers < 120:
        discount = -0.15
elif kind_flower == "Gladiolus":
    flower_price = 2.5
    if count_flowers < 80:
        discount = -0.2

final_flower_price = count_flowers * flower_price * (1 - discount)

diff = abs(budget - final_flower_price)
if budget >= final_flower_price:
    print(f"Hey, you have a great garden with {count_flowers} {kind_flower} and {diff:.2f} leva left.")
elif budget < final_flower_price:
    print(f"Not enough money, you need {diff:.2f} leva more.")