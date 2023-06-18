import sys

n = int(input())
pair_count = [0] * 10

for _ in range(n):
    student_schedule = list(map(int, sys.stdin.readline().split()))
    index = 0
    for i in range(5):
        for j in range(i + 1, 5):
            pair_count[index] += student_schedule[i] & student_schedule[j]
            index += 1

first, second = 0, 1
max_students = pair_count[0]
index = 0
for i in range(5):
    for j in range(i + 1, 5):
        if pair_count[index] > max_students:
            first = i
            second = j
            max_students = pair_count[index]
        index += 1
answer = [0] * 5
answer[first] = answer[second] = 1

print(max_students)
print(*answer)
