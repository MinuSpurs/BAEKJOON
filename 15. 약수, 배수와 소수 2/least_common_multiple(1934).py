import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    temp = min(a,b)
    while True:
        if a % temp == 0 and b % temp == 0:
            print((a*b)//temp)
            break
        else:
            temp -= 1