turns = int(input())

result = 0
count_0 = 0
count_10 = 0
count_20 = 0
count_30 = 0
count_40 = 0
count_negative = 0

for every_turn in range(1, turns + 1):
    number = int(input())
    if number < 0:
        result /= 2
        count_negative += 1
    elif 0 <= number <= 9:
        result += number * 0.2
        count_0 += 1
    elif 10 <= number <= 19:
        result += number * 0.3
        count_10 += 1
    elif 20 <= number <= 29:
        result += number * 0.4
        count_20 += 1
    elif 30 <= number <= 39:
        result += 50
        count_30 += 1
    elif 40 <= number <= 50:
        result += 100
        count_40 += 1
    else:
        result /= 2
        count_negative += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {(count_0 / turns) * 100:.2f}%")
print(f"From 10 to 19: {(count_10 / turns) * 100:.2f}%")
print(f"From 20 to 29: {(count_20 / turns) * 100:.2f}%")
print(f"From 30 to 39: {(count_30 / turns) * 100:.2f}%")
print(f"From 40 to 50: {(count_40 / turns) * 100:.2f}%")
print(f"Invalid numbers: {(count_negative / turns) * 100:.2f}%")