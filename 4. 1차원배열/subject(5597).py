student_list = []

for i in range(28):
    student = int(input())
    student_list.append(student)

student_list = set(student_list)
sub_list = set(range(1,31))
student_list = list(sub_list - student_list)

student_list.sort()

for i in student_list:
    print(i)