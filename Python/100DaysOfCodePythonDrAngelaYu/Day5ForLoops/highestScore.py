student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,55,91,64,89]

total_exam_score = sum(student_scores)

for_sum = 0
for score in student_scores:
    for_sum += score

print("Python sum: ", total_exam_score)
print("For sum: ", for_sum)

max_student_score = max(student_scores)

for_max = student_scores[1]

for i in student_scores:
    if i > for_max:
        for_max = i

print("Python max: ", max_student_score)
print("For max: ", for_max)

# Dr Angela Wu solution

dr_max = 0

for score in student_scores:
    if score > dr_max:
        dr_max = score

print(dr_max)











