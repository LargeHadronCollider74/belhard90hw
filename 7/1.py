"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""

assessments = list()
print("Input student assessment (0 for exit)")
while True:
    assessment = int(input(f"assessment {len(assessments) + 1}:"))
    if (0 == assessment):
        break
    assessments.append(assessment)

print(f"Assessment: {assessments}", f"Average: {sum(assessments) / len(assessments):.01f}", sep="\n")
    