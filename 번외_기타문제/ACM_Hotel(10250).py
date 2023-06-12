import sys

T = int(input())

for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())

    cnt = 1
    while N > H:
        if N > H:
            N = N - H
            cnt += 1

    if cnt < 10:
        cnt = '0' + str(cnt)
    else:
        cnt = str(cnt)

    print(int(str(N) + cnt))