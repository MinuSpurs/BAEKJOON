import sys

n = int(input())
name_dict = {}

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    if a in name_dict or b in name_dict:
        name_dict[a] = i
        name_dict[b] = i
    elif a == 'ChongChong' or b == 'ChongChong':
        name_dict[a] = i
        name_dict[b] = i

print(len(name_dict))