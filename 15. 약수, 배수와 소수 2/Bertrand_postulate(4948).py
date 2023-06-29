import sys

def era(n):
    primes = [True] * (2*n + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int((2*n)**0.5)+1):
        if primes[i]:
            for j in range(i*i, 2*n+1, i):
                primes[j] = False

    return primes

while True:
    cnt = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break
    primes = era(n)
    cnt = sum(primes[n+1:2*n+1])
    print(cnt)