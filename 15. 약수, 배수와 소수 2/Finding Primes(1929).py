def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

m, n = map(int, input().split())

while True:
    if m >= (n+1):
        break
    if is_prime(m):
        print(m)
    m += 1