hour = int(input())
day_from_week = input()

if 10 <= hour <= 18 and day_from_week != "Sunday":
    print("open")
else:
    print("closed")