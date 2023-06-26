a, b, c = map(int, input().split())

arr = [a, b, c]

for i in range(2, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(*arr)