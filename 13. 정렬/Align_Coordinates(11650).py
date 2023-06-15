import sys

N = int(input())
coor = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    coor.append(temp)

coor.sort()

for i in range(len(coor)):
    print(coor[i][0], coor[i][1])