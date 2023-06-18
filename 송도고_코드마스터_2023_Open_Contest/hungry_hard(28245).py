import sys

n = int(input())
for i in range(n):
    m = int(sys.stdin.readline())
    a = b = 0
    min_diff = 1 << 61

    for y in range(60):
        for x in range(y + 1):
            diff = abs((1 << x) + (1 << y) - m)
            if diff < min_diff:
                min_diff = diff
                a = x
                b = y
    print(a, b)
