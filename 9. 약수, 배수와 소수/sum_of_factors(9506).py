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
    print(value, temp)
    if value == n:
        print('perfect')
    else:
        print('not perfect')