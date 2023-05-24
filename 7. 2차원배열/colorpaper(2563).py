import sys

N = int(input())

matrix = []
result = 100

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

matrix.sort()
i = 0

while(i<=N):
    for j in range(i, N):
        if i == j:
            continue
        if matrix[i][0] <= matrix[j][0] and (matrix[i][0] + 10) >= matrix[j][0]:
            result += (100 - (10 - (matrix[j][0] - matrix[i][0])) * (10 - abs((matrix[j][1] - matrix[i][1]))))
            i += 1
        else:
            result += 100
            i += 1
    i += 1

print(result)