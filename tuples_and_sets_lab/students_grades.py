students_count = int(input())
students_grades = {}
for _ in range(students_count):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

for s, g in students_grades.items():
    average_grade = sum(g) / len(g)
    g = [f'{x:.2f}' for x in g]
    print(f"{s} -> {' '.join(g)} (avg: {average_grade:.2f})")
