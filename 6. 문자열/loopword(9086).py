T = int(input())

array = []
for i in range(T):
    word = input()
    array.append(word)

for i in range(T):
    print(array[i][0] + array[i][-1])
