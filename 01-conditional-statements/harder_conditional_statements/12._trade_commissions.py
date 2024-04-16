town = input()
volume_sales = float(input())
commission = 0

if town == "Sofia":
    if 0 <= volume_sales <= 500:
        commission = 0.05
    elif 500 < volume_sales <= 1000:
        commission = 0.07
    elif 1000 < volume_sales <= 10000:
        commission = 0.08
    elif volume_sales > 10000:
        commission = 0.12
if town == "Varna":
    if 0 <= volume_sales <= 500:
        commission = 0.045
    elif 500 < volume_sales <= 1000:
        commission = 0.075
    elif 1000 < volume_sales <= 10000:
        commission = 0.10
    elif volume_sales > 10000:
        commission = 0.13
if town == "Plovdiv":
    if 0 <= volume_sales <= 500:
        commission = 0.055
    elif 500 < volume_sales <= 1000:
        commission = 0.08
    elif 1000 < volume_sales <= 10000:
        commission = 0.12
    elif volume_sales > 10000:
        commission = 0.145
if volume_sales < 0 or town != "Sofia" and town != "Varna" and town != "Plovdiv":
    print("error")
else:
    commission = commission * volume_sales
    print(f"{commission:.2f}")