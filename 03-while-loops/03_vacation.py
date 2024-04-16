price_vacation = float(input()) #2000 струва ваканцията
current_money = float(input()) # започва деня с 1000 налични
all_days = 0 # брояч на дните
spending_counter = 0 # брояч на дните, в които харчи
total_money = current_money
is_failed = False

while True:
    all_days += 1
    activity = input() # има команда да харчи
    sum_spend_save = float(input())

    if activity == "spend":
        spending_counter += 1
        if spending_counter >= 5:
            is_failed = True
            break
        total_money -= sum_spend_save
        if total_money <= 0:
            total_money = 0
    elif activity == "save":
        spending_counter = 0
        total_money += sum_spend_save
        if total_money >= price_vacation:
            break

if not is_failed:
    print(f"You saved the money for {all_days} days.")
else:
    print("You can't save the money.")
    print(f"{all_days}")