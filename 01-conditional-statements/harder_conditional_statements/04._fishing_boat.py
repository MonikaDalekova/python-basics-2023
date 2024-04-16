budget = int(input())
season = input()
count_fishers = int(input())

rent_a_ship = 0
discount = 0

if season == "Spring":
    rent_a_ship = 3000
elif season == "Summer" or "Autumn":
    rent_a_ship = 4200
elif season == "Winter":
    rent_a_ship = 2600

if count_fishers <= 6:
    discount = 0.1
elif 7 <= count_fishers <= 11:
    discount = 0.15
elif count_fishers >= 12:
    discount = 0.25

extra_discount = 0
if count_fishers % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_cost = rent_a_ship * (1 - discount) * (1 - extra_discount)

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")