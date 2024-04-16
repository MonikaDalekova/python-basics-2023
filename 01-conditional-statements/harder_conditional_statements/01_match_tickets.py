budget = float(input())
type_ticket = input()
count_people = int(input())

transport_price = 0
price_ticket = 0

if count_people <= 4:
    transport_price = budget * 0.75
elif 4 < count_people <= 9:
    transport_price = budget * 0.60
elif 9 < count_people <= 24:
    transport_price = budget * 0.5
elif 24 < count_people <= 49:
    transport_price = budget * 0.4
else:
    transport_price = budget * 0.25

if type_ticket == "VIP":
    price_ticket = 499.99 * count_people
elif type_ticket == "Normal":
    price_ticket = 249.99 * count_people

left_money = budget - transport_price

diff = abs(left_money - price_ticket)

if left_money >= price_ticket:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")