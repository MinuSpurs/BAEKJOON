import sys

def era(n):
    arr = [True] * (n+1)
    arr[0], arr[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False

    return arr

def goldbach_partition(n, prime):
    cnt = 0

    for i in range(2, (n//2)+1):
        if prime[i] and prime[n-i]:
            cnt += 1

    return cnt


n = int(input())
primes = era(1000000)

for i in range(n):
    temp = int(sys.stdin.readline())
    print(goldbach_partition(temp, primes))