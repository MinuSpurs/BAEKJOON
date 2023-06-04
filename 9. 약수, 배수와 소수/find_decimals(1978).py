import sys

N = int(input())

array = list(map(int, sys.stdin.readline().split()))
demical = []

for i in range(N):
    if array[i] == 1:
        continue
    demical.append(array[i])
    for j in range(2, array[i]):
        if array[i] % j == 0:
            demical.remove(array[i])
            break
    

print(len(demical))
