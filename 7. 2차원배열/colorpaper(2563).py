import sys

N = int(input())

matrix = []
result = 100

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

matrix.sort()
i = 0
x1, x2 = matrix[0][0], matrix[0][0] + 10
y1, y2 = matrix[0][1], matrix[0][1] + 10

while(i<=N):
    for j in range(i, N):
        if i == j:
            continue
        if x1 <= matrix[j][0] and (x1 + 10) >= matrix[j][0]:
            result += (100 - ((x2 + x1) - (matrix[j][0] - x1)) * ((y2 + y1) - abs((matrix[j][1] - y1))))
            x1 = matrix[j][0] - x1
            x2 = x1 + 10
            y1 = abs((matrix[j][1] - y1))
            y2 = y1 + 10
            i += 1
        else:
            result += 100
            i += 1
    i += 1

print(result)