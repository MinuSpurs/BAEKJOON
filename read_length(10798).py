import sys

matrix = []
for i in range(5):
    matrix.append(list(sys.stdin.readline().split()))

for i in range(5):
    if len(matrix[i]) < 15:
        for j in range(15 - len(matrix[i])):
            matrix[i].append('.')

print(matrix)
for i in range(15):
    for j in range(5):
        if matrix[j][i] == '.':
                continue
        for k in range(len(matrix[j][i])):          
            print(matrix[j][i][k], end='')