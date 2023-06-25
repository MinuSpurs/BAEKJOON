A, B = map(int, input().split())
C, D = map(int, input().split())

a, b = B, D
while b > 0:
    a, b = b, a%b

up = ((A * D) // a) + ((C * B) // a)
down = (B * D) // a

print(up, down)
a, b = up, down
while b > 0:
    a, b = b, a%b

print(a)

if a != 1:
    up /= a
    down /= a

print(int(up), int(down))
