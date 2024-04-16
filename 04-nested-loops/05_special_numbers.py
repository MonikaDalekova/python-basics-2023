number = int(input())

for n in range(1_111, 10_000):
    n_as_string = str(n)  # "1111"

    is_special = True
    for _, digit in enumerate(n_as_string):  # n -> 1_111, ..., 9_999
        digit_as_int = int(digit)  # int("1") == 1

        if digit_as_int == 0: # не можем да делим на 0 и като се подаде число 0, получаваме грешка
            is_special = False # по-лесно е да видим кои числа не са специални и да бреакваме цикъла с тях
            break

        if number % digit_as_int != 0:
            is_special = False
            break

    if is_special: # след като сме махнали не специалните числа, остава да печатаме само специалните
        print(f"{n} ", end="")