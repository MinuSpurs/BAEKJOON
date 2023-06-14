N = input()

arr = []
count = [0] * 10
sorted_list = []

for i in range(len(N)):
    arr.append(int(N[i]))

for i in range(len(N)):
    count[arr[i]] += 1

for i in range(9, -1, -1):
    if count[i] != 0:
        for j in range(count[i]):
            sorted_list.append(i)

for i in range(len(sorted_list)):
    print(sorted_list[i], end='')