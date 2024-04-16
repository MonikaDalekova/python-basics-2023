age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
total_toys = 0

for birthday in range (0, age):
    if birthday % 2 == 0:
        current_money = birthday * 5
        total_money += current_money
        total_money -= 1
    else:
        total_toys += 1

toys_money = total_toys * toy_price
total_money += toys_money

diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")