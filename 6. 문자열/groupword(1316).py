N = int(input())

array = []
for i in range(N):
    word = input()
    array.append(word)
temp = []
i = 0
j = 0
cnt = 0
while(i < len(array)):
    if array[i][j] not in temp:
        temp.append(array[i][j])
        if j >= len(array[i]) - 1:
            cnt = cnt + 1
            i = i + 1
            j = 0
            temp = []
            continue
        j = j + 1
    elif array[i][j] == temp[j-1]:
        if j == len(array[i]) - 1:
            cnt = cnt + 1
            i = i + 1
            j = 0
            temp = []
            continue
        temp.append(array[i][j])
        j = j + 1
    else:
        i = i + 1
        j = 0
        temp = []

print(cnt)