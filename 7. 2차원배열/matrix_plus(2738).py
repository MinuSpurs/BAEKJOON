import sys

N, M = map(int, input().split())

result = []
matrix_1 = []
matrix_2 = []
for j in range(N):
    matrix_1.append(list(map(int, sys.stdin.readline().split())))
for j in range(N):
    matrix_2.append(list(map(int, sys.stdin.readline().split())))

'''for i in range(N):
    result.append([])
    for j in range(M):
        result[i].append(matrix_1[i][j] + matrix_2[i][j])
        print(result[i][j], end=' ')
    print()'''

print(matrix_1 + matrix_2)