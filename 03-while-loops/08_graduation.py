name_student = input()
current_classes = 1
bad_grades = 0
total_grade = 0
is_expelled = False

while current_classes <= 12:
    annual_grade = float(input())
    if annual_grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            is_expelled = True
            break
        continue
    current_classes += 1
    total_grade += annual_grade
if is_expelled == "True":
    print(f"{name_student} has been excluded at {current_classes} grade")
else:
    av_grade = total_grade / 12
    print(f"{name_student} graduated. Average grade: {av_grade:.2f}")