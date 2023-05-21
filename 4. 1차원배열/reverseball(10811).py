N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(i+1)

for i in range(M):
    i, j = map(int, input().split())
    temp = 0
    while(i<j):
        temp = basket[i-1]
        basket[i-1] = basket[j-1]
        basket[j-1] = temp
        i = i+1
        j = j-1

for i in range(N):
    print(basket[i], end=' ')