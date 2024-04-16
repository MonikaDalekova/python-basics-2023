n = int(input())
current = 1  # брояч колко числа сме отпечатали
is_current_bigger_than_n = False
for row in range(0, n + 1): # за всеки ред в интервала от 0 до числото N:
    for col in range (0, row + 1): # за всяко число в интервала от 0 до броя редове:
        if current > n: # ако броя отпечатани числа е по-голям от даденото число n:
            is_current_bigger_than_n = True # булевата става вярна и прекъсваме цикъла
            break
        print(str(current) + " ", end="")
        current += 1 # броячът се увеличава с още едно число
    if is_current_bigger_than_n: # ако броят въведени числа е повече от числото N, прекъсваме
        break
    print()
