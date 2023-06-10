N, M = map(int, input().split())
array = list(map(int, input().split()))

array = sorted(array, reverse=True)

value = array[0] + array[1] + array[2]
temp = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            value = array[i] + array[j] + array[k]
            if value <= M:
                temp.append(value)

print(max(temp))