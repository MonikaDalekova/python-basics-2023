odd_min = 1000000000.0
odd_max = -1000000000.0
even_min = 1000000000.0
even_max = -1000000000.0
odd_counter = 0
even_counter = 0
count_numbers = int(input())
odd_sum = 0
even_sum = 0
counter = 0
for _ in range(1, count_numbers + 1):
    current_number = float(input())
    counter += 1
    if counter % 2 == 0:
        even_sum += current_number
        even_counter += 1
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        odd_counter += 1
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number
if even_counter == 0:
    even_max = "No"
    even_min = "No"
if odd_counter == 0:
    odd_max = "No"
    odd_min = "No"

print(f"OddSum={odd_sum :.2f},")
if odd_counter != 0:
    print(f"OddMin={odd_min :.2f},")
    print(f"OddMax={odd_max :.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")
print(f"EvenSum={even_sum :.2f},")
if even_counter != 0:
    print(f"EvenMin={even_min :.2f},")
    print(f"EvenMax={even_max :.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
