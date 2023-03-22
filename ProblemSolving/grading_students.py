import math


def gradingStudents(grades):
    res = []
    for grade in grades:
        final_grade = math.ceil(grade / 5) * 5
        if final_grade - grade >= 3 or grade < 38:
            res.append(grade)
        else:
            res.append(final_grade)

    return res


grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print('\n'.join(map(str, result)))
print('\n')
