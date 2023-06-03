import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    temp = []
    for i in range(1,n):
        if n % i == 0:
            temp.append(i)
    value = 0
    for i in range(len(temp)):
        value += temp[i]

    if value == n:
        print(n, '=',end=' ')
        for i in range(len(temp)):
            if temp[i] != temp[-1]:
                print(temp[i],'+', end=' ')
            else:
                print(temp[i])
    else:
        print(n, 'is NOT perfect.')