import sys

r, c = map(int, sys.stdin.readline().split())

dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in range(r):
    kayak = sys.stdin.readline().rstrip()
    for j in range(c-2, 1, -1):
        if kayak[j] != '.':
            dic[int(kayak[j])] = j
            break

sorted_keys = sorted(dic, key=dic.get, reverse=True)

print(sorted_keys)

rank = 1
prev_value = dic[sorted_keys[0]]
ranking = {}
for key in sorted_keys:
    if dic[key] != prev_value:
        rank += 1
    ranking[key] = rank
    prev_value = dic[key]

ranking_in_order = {key: ranking[key] for key in dic}

for i in range(len(ranking_in_order)):
    print(ranking_in_order[i+1])