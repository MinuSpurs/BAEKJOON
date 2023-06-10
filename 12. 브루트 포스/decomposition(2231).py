N = int(input())
temp = N
value = temp
array = []

for i in range(N):
    for j in range(len(str(temp))):
        value += int(str(temp)[j])
    if value == N:
        array.append(temp)
    temp -= 1
    value = temp

if len(array) == 0:
    print('0')
else:
    print(min(array))