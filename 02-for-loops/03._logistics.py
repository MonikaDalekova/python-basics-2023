count_loads = int(input())

total_price = 0
weight_microbus = 0
weight_truck = 0
weight_train = 0
count_weight = 0

for every_load in range(1, count_loads + 1):
    weight_load = int(input())
    count_weight += weight_load
    if weight_load <= 3:
        price = 200 * weight_load
        weight_microbus += weight_load
        total_price += price
    elif 4 <= weight_load <= 11:
        price = 175 * weight_load
        weight_truck += weight_load
        total_price += price
    else:
        price = 120 * weight_load
        weight_train += weight_load
        total_price += price
av_price = total_price / count_weight
percent_microbus = weight_microbus / count_weight * 100
percent_truck = weight_truck / count_weight * 100
percent_train = weight_train / count_weight * 100
print(f"{av_price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")