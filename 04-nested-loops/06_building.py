number_of_floors = int(input())
number_of_rooms = int(input())
floor_letter = ""
for current_floor in range(number_of_floors, 0, -1):
    if current_floor == number_of_floors:  # Намираме се на последния етаж
        floor_letter = "L"
    elif current_floor % 2 == 0:  # Намираме се на четен етаж
        floor_letter = "O"
    else:  # elif current_floor %2 != 0: Намираме се на нечетен етаж
        floor_letter = "A"
    for current_room in range(number_of_rooms):
        print(f"{floor_letter}{current_floor}{current_room}", end=" ")
    print() # изпраща ни на следващ ред за всеки отделен етаж