import sys

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

T = int(input())

for i in range(T):
    n = int(sys.stdin.readline())
    while not is_prime(n):
        n += 1
    print(n)