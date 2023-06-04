import sys

N = int(input())

array = list(map(int, sys.stdin.readline().split()))
demical = []

for i in range(N):
    if array[i] == 1:
        continue
    for j in range(1, array[i]):
        if array[i] % j == 0:
            demical.append(array[i])
        else:
            break

print(demical)
