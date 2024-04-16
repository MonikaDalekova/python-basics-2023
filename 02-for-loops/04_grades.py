count_students = int(input())
lowest_grades_students = 0
low_grades_students = 0
average_grade_students = 0
excellent_grades_students = 0
grades = 0
for every_student in range(1, count_students + 1):
    exam_grade = float(input())
    grades += exam_grade
    if 2 <= exam_grade <= 2.99:
        lowest_grades_students += 1
    elif 3 <= exam_grade <= 3.99:
        low_grades_students += 1
    elif 4 <= exam_grade <= 4.99:
        average_grade_students += 1
    else:
        excellent_grades_students += 1
av_grade = grades / count_students
percent_lowest = lowest_grades_students / count_students * 100
percent_low = low_grades_students / count_students * 100
percent_average = average_grade_students / count_students * 100
percent_excellent = excellent_grades_students / count_students * 100
print(f"Top students: {percent_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percent_average:.2f}%")
print(f"Between 3.00 and 3.99: {percent_low:.2f}%")
print(f"Fail: {percent_lowest:.2f}%")
print(f"Average: {av_grade:.2f}")