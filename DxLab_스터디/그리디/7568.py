n = int(input())

student_list = [[] for _ in range(n)]

rank_list = [0 for _ in range(n)]

for i in range(n):
    student_list[i] = list(map(int, input().split()))

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if student_list[i][0] < student_list[j][0]:
            if student_list[i][1] >= student_list[j][1]:
                continue
            elif student_list[i][1] < student_list[j][1]:
                rank += 1

        elif student_list[i][1] < student_list[j][1]:
            if student_list[i][0] >= student_list[j][0]:
                continue
            elif student_list[i][0] < student_list[j][0]:
                rank += 1
                
        elif student_list[i][0] == student_list[j][0]:
            if student_list[i][1] < student_list[j][1]:
                rank += 1

        elif student_list[i][1] == student_list[j][1]:
            if student_list[i][0] < student_list[j][0]:
                rank += 1
    rank_list[i] = rank

print(*rank_list)