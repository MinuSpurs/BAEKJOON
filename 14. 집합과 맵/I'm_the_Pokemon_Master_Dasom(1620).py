import sys

N , M = map(int, input().split())

dogam = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    dogam[i+1] = name

reverse_dogam = dict(map(reversed, dogam.items()))

for _ in range(M):
    search = sys.stdin.readline().rstrip()
    try:
        print(dogam[int(search)])
    except:
        print(reverse_dogam[search])