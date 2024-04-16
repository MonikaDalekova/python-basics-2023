budget = float(input())
season = input()

price = 0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = 0.3
    elif season == "winter":
        price = 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = 0.4
    elif season == "winter":
        price = 0.8
elif budget > 1000:
    destination = "Europe"
    if season == "summer" or season == "winter":
        price = 0.9

if destination == "Europe":
    place = "Hotel"
elif destination == "Bulgaria" or destination == "Balkans":
    if season == "summer":
        place = "Camp"
    elif season == "winter":
        place = "Hotel"

total_price = price * budget

print(f"Somewhere in {destination}")
print(f"{place} - {total_price:.2f}")