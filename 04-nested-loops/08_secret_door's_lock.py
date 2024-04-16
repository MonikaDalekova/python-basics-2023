upper_limit_hundreds = int(input())
upper_limit_tens = int(input())
upper_limit_ones = int(input())

for hundreds in range(2, upper_limit_hundreds + 1, 2):
    for tens in range(2, upper_limit_tens + 1):
        for ones in range(2, upper_limit_ones + 1, 2):
            is_prime = True
            for div in range(2, tens):
                if tens % div == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"{hundreds} {tens} {ones}")

