import sys

n = int(sys.stdin.readline())

res = {}

for i in range(n):
    file = sys.stdin.readline().rstrip()
    file = file.split('.')
    ext = file[1]
    if ext in res:
        res[ext] += 1
    else:
        res[ext] = 1


for key, value in sorted(res.items()):
    print(key, value)