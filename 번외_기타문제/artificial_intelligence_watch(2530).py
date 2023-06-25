a, b, c = map(int, input().split())
time = int(input())

hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60

a += hour
b += minute
c += second

if c >= 60:
    c -= 60
    b += 1
if b >= 60:
    b -= 60
    a += 1
if a >= 24:
    a %= 24

print(a, b, c)