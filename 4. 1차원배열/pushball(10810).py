N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(0)

for a in range(M):
    i, j, k = map(int, input().split())
    for j in range(i-1, j):
        basket[j] = k

for i in range(N):
    print(basket[i], end=' ')