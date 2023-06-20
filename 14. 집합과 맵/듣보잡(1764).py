import sys

N, M = map(int, input().split())

name_dict = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    name_dict[name] = 1

for i in range(M):
    name = sys.stdin.readline().rstrip()
    if name in name_dict.keys():
        name_dict[name] += 1
    else:
        name_dict[name] = 1

count = 0

for key in name_dict:
    if name_dict[key] == 2:
        count+=1

sorted_name = sorted(name_dict.items())

print(count)
for key, value in sorted_name:
    if value == 2:
        print(key)