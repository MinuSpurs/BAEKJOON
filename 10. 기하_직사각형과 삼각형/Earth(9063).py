import sys

N = int(input())
x_temp, y_temp = [], []
for i in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    x_temp.append(x[0])
    y_temp.append(x[1])

width = (max(x_temp) - min(x_temp)) * (max(y_temp) - min(y_temp))

print(width)