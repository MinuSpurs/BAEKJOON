import sys

matrix = []

for i in range(9):
    matrix.append(list(map(int, sys.stdin.readline().split())))

x, y = 1, 1
max = matrix[0][0]
for i in range(9):
    for j in range(9):
        if max < matrix[i][j]:
            max = matrix[i][j]
            x = i + 1
            y = j + 1


print(max)
print(x, y)