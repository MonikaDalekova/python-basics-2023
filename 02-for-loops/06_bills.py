count_months = int(input())

count_electricity = 0
count_water = 0
count_internet = 0
count_other = 0

for every_month in range(1, count_months + 1):
    electricity = float(input())
    count_electricity += electricity
    count_water += 20
    count_internet += 15
    other = (electricity + 20 + 15) * (1 + 0.2)
    count_other += other
total_expense = count_other + count_water + count_internet + count_electricity
av_sum = total_expense / count_months
print(f"Electricity: {count_electricity:.2f} lv")
print(f"Water: {count_water:.2f} lv")
print(f"Internet: {count_internet:.2f} lv")
print(f"Other: {count_other:.2f} lv")
print(f"Average: {av_sum:.2f} lv")