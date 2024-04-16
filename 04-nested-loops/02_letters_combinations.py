start_letter = input()
final_letter = input()
not_included = input()
combination_counter = 0

start_letter_int = ord(start_letter)
final_letter_int = ord(final_letter)
not_included_int = ord(not_included)
for first_digit in range(start_letter_int, final_letter_int + 1):
    for second_digit in range(start_letter_int, final_letter_int + 1):
        for third_digit in range(start_letter_int, final_letter_int + 1):
            if first_digit == not_included_int or second_digit == not_included_int or third_digit == not_included_int:
                continue
            else:
                combination_counter += 1

            first_digit_str = chr(first_digit)
            second_digit_str = chr(second_digit)
            third_digit_str = chr(third_digit)
            print(f"{first_digit_str}{second_digit_str}{third_digit_str} ", end="")
print(f"{combination_counter}")