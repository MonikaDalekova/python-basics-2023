count_juniors = int(input())
count_seniors = int(input())
kind_trace = input()

discount = 0

if kind_trace == "trail":
    tax = count_juniors * 5.50 + count_seniors * 7
elif kind_trace == "cross-country":
    tax = count_juniors * 8 + count_seniors * 9.50
elif kind_trace == "downhill":
    tax = count_juniors * 12.25 + count_seniors * 13.75
elif kind_trace == "road":
    tax = count_juniors * 20 + count_seniors * 21.50

all_runners = count_seniors + count_juniors
all_tax = tax - (tax * 0.05)

if kind_trace == "cross-country" and all_runners >= 50:
    discount = 0.25

total_tax = all_tax - (all_tax * discount)

print(f"{total_tax:.2f}")