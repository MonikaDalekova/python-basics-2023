n = int(input())
all = 0
for number in range(1, n + 1):
    current_number = int(input())
    all += current_number
av = all / n
print(f"{av:.2f}")

