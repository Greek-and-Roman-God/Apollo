# 시험 성적
score = int(input())
grade = ""
if score > 89:
    grade = "A"
elif score > 79:
    grade = "B"
elif score > 69:
    grade = "C"
elif score > 59:
    grade = "D"
else:
    grade = "F"
print(grade)