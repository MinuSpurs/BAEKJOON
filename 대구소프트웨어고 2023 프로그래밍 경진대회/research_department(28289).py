import sys

n = int(input())

soft, embe, ai, jr = 0, 0, 0, 0

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        jr += 1
    else:
        if b == 1 or b == 2:
            soft += 1
        elif b == 3:
            embe += 1
        elif b == 4:
            ai += 1

print(soft)
print(embe)
print(ai)
print(jr)