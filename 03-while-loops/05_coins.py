target_amount = float(input())
count_coins = 0
target_amount_levas = int(target_amount * 100)

while target_amount_levas > 0:
    if target_amount_levas >= 200:
        target_amount_levas -= 200
        count_coins += 1
    elif target_amount_levas >= 100:
        target_amount_levas -= 100
        count_coins += 1
    elif target_amount_levas >= 50:
        target_amount_levas -= 50
        count_coins += 1
    elif target_amount_levas >= 20:
        target_amount_levas -= 20
        count_coins += 1
    elif target_amount_levas >= 10:
        target_amount_levas -= 10
        count_coins += 1
    elif target_amount_levas >= 5:
        target_amount_levas -= 5
        count_coins += 1
    elif target_amount_levas >= 2:
        target_amount_levas -= 2
        count_coins += 1
    elif target_amount_levas >= 1:
        target_amount_levas -= 1
        count_coins += 1

print(count_coins)