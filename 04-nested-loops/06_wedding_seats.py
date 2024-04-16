last_sector = input()
count_rows_first_sector = int(input())
count_odd_row_seats = int(input())

last_sector_int = ord(last_sector)
seat_counter = 0

for every_sector in range(65, last_sector_int + 1):
    sector = chr(every_sector)
    for every_row in range(1, count_rows_first_sector + 1):
        if every_row % 2 != 0:
            for every_seat in range(97, (97 + count_odd_row_seats)):
                every_seat_str = chr(every_seat)
                print(f"{sector}{every_row}{every_seat_str}")
                seat_counter += 1
        elif every_row % 2 == 0:
            for every_seat in range(97, (97 + count_odd_row_seats + 2)):
                every_seat_str = chr(every_seat)
                print(f"{sector}{every_row}{every_seat_str}")
                seat_counter += 1
    count_rows_first_sector += 1
print(seat_counter)