import sys

N = int(input())

matrix = []
result = N * 100

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if result <= 100:
            break
        if (matrix[i][0] <= matrix[j][0] and matrix[i][0] + 10 >= matrix[j][0]):
            print("위조건", i,j, (matrix[i][0] + 10) - matrix[j][0], 10 - (abs(matrix[i][1] - matrix[j][1])))
            temp = ((matrix[i][0] + 10) - matrix[j][0]) * (10 - (abs(matrix[i][1] - matrix[j][1])))
            result -= temp
        
print(result)