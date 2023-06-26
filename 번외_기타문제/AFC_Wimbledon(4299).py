add, dele = map(int, input().split())

a = (add + dele) / 2
b = (add - dele) / 2

if dele > add or a % 1 != 0 or b % 1 != 0:
    print(-1)
else:
    a, b = int(a), int(b)
    if a >= b:
        print(a, b)
    else:
        print(b, a)