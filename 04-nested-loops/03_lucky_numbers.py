number = int(input())

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for forth_digit in range(1, 10):
                left_sum = first_digit + second_digit
                right_sum = third_digit + forth_digit
                if left_sum == right_sum and number % left_sum == 0:
                    print(f"{first_digit}{second_digit}{third_digit}{forth_digit} ", end="")