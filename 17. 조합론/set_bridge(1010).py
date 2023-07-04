import sys

def factorial(n):
    result = 1
    if n > 1:
        result = n * factorial(n-1)
    else:
        return 1
    return result

T = int(input())

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    result = factorial(m) // (factorial(n) * factorial(m - n))
    print(result)