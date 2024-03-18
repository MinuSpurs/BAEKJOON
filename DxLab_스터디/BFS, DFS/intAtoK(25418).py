A, K = map(int, input().split())

count = 0
while A < K:
    if K % 2 == 0:
        K //= 2
    else:
        K -= 1
    count += 1

count += A - K
print(count)
