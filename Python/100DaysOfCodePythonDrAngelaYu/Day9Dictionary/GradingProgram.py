student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for value in student_scores:
    if student_scores[value] >= 91:
        student_grades[value] = "Outstanding"
    elif student_scores[value] >= 81:
        student_grades[value] = "Exceeds Expectations"
    elif student_scores[value] >= 71:
        student_grades[value] = "Acceptable"
    else:
        student_grades[value] = "Fail"

print(student_grades)
