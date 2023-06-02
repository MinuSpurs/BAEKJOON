N, K = map(int, input().split())

array = []

for i in range(1, N+1):
    if N % i == 0:
        array.append(i)

try:
    print(array[K-1])
except:
    print(0)