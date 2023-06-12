import sys

N = int(input())
array = [-1]

for i in range(N):
    num = int(sys.stdin.readline())
    array.append(num)

for i in range(N, 0, -1):
    for j in range(1, i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


for i in range(1, N+1):
    print(array[i])