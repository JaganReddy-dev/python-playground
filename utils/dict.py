student_names = ("Ashley", "David", "Edward", "Zoe")
exam_grades = (0.92, 0.72, 0.88, 0.77)

student_grades = dict(zip(student_names, exam_grades))
print(student_grades)
student_grades["Zoe"] = 0.79
print(student_grades)
student_grades["Ryan"] = 0.34
print(student_grades)
