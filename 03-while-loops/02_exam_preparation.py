count_bad_grades_limit = int(input())
count_bad_grades = 0
all_grades = 0
last_problem = ""
all_sum_grades = 0

command = input()

while command != "Enough":
    next_text = command
    current_grade = int(input())
    all_grades += 1
    all_sum_grades += current_grade
    last_problem = next_text
    if current_grade <= 4:
        count_bad_grades += 1
        if count_bad_grades >= count_bad_grades_limit:
            break

    command = input()

if command == "Enough":
    avg = all_sum_grades / all_grades
    print(f"Average score: {avg:.2f}")
    print(f"Number of problems: {all_grades}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {count_bad_grades} poor grades.")