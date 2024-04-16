first_number_range = int(input())
second_number_range = int(input())
third_number_range = int(input())

for first_number in range(2, first_number_range + 1, 2):
    for second_number in range(2, second_number_range + 1):
        for third_number in range(2, third_number_range + 1, 2):
            is_second_prime = True
            for div in range(2, second_number):
                if second_number % div == 0:
                    is_second_prime = False
                    break
            if is_second_prime:
                print(f'{first_number} {second_number} {third_number}')