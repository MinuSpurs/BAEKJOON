import sys

n = int(input())

i = 1
cnt = 0
name_dict = {}
while i <= n:
    name = sys.stdin.readline().rstrip()
    if name == 'ENTER':
        cnt += len(name_dict)
        name_dict = {}
        i += 1
    else:
        name_dict[name] = i
        i += 1
cnt += len(name_dict)

print(cnt) 
    