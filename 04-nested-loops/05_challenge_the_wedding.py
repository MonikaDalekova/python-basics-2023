men = int(input())
women = int(input())
max_count_tables = int(input())
counter_meeting = 0

for every_man in range(1, men + 1):
    for every_woman in range(1, women + 1):
        counter_meeting += 1
        if counter_meeting > max_count_tables:
            break
        print(f"({every_man} <-> {every_woman}) ", end="")