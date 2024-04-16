screening_type = input()
rows = int(input())
columns = int(input())
price = 0

cinema_capacity = rows * columns

if screening_type == "Premiere":
    price = cinema_capacity * 12
elif screening_type == "Normal":
    price = cinema_capacity * 7.50
elif screening_type == "Discount":
    price = cinema_capacity * 5

print(f"{price:.2f} leva")