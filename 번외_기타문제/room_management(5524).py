import sys

N = int(input())

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    print(name.lower())