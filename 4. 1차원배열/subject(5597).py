student_list = []
dont_student = []

for i in range(28):
    student = int(input())
    student_list.append(student)

student_list.sort()

for i in range(27):
    if student_list[i+1] - student_list[i] != 1:
        dont_student.append(student_list[i]+1)
        if student_list[i+1] - student_list[i] == 3:
            dont_student.append(student_list[i]+2)
    if len(dont_student) == 1:
        dont_student.append(30)
    elif len(dont_student) == 0:
        dont_student.append(29)
        dont_student.append(30)

print(dont_student[0])
print(dont_student[1])