expected_cash = int(input())
cash_payment = 0
card_payment = 0
payment_counter = 0
number_of_cash_payments = 0
number_of_card_payments = 0

command = input()
while command != 'End':
    items_price = int(command)
    payment_counter += 1
    if payment_counter % 2 == 0:
        if items_price < 10:
            card_payment += 0
            print(f'Error in transaction!')
        else:
            card_payment += items_price
            number_of_card_payments += 1
            print('Product sold!')
    else:
        if items_price > 100:
            cash_payment += 0
            print(f'Error in transaction!')
        else:
            cash_payment += items_price
            number_of_cash_payments += 1
            print('Product sold!')
    if expected_cash == cash_payment + card_payment or expected_cash < cash_payment + card_payment:
        break
    command = input()

if expected_cash <= cash_payment + card_payment:
    average_cash = cash_payment / number_of_cash_payments
    average_card = card_payment / number_of_card_payments
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")

if command == 'End':
    print("Failed to collect required money for charity.")