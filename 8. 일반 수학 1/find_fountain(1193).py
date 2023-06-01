import math

x = int(input())

a = 1
b = 1
c = -x * 2

r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
s = ((2 + (math.ceil(r1) - 1)) * math.ceil(r1)) / 2
up, down = 1, 1

if math.ceil(r1) % 2 == 0:
    up = math.ceil(r1)
    i = int(s) - x
    while i > 0:
        up -= 1
        down += 1
        i -= 1
elif math.ceil(r1) % 2 == 1:
    down = math.ceil(r1)
    i = int(s) - x
    while i > 0:
        down -= 1
        up += 1
        i -= 1

print(str(up)+'/'+str(down))