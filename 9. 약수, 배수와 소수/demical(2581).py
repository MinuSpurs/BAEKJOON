M = int(input())
N = int(input())

demical = []
temp = []
result = 0

for i in range(M, N + 1):
    temp.append(i)

for i in range(len(temp)):
    if temp[i] == 1:
        continue
    demical.append(temp[i])
    for j in range(2, temp[i]):
        if temp[i] % j == 0:
            demical.remove(temp[i])
            break

for i in range(len(demical)):
    result += demical[i]

if len(demical) > 0:
    print(result)
    print(min(demical))
else:
    print('-1')

