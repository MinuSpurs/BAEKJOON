S = input()

place = [-1 for i in range(26)]

for i in range(len(S)):
    asc = ord(S[i]) - 97
    if place[asc] == -1:
        place[asc] = i

for i in range(len(place)):
    print(place[i], end=' ')