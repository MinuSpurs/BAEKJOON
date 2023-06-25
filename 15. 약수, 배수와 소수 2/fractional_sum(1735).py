A, B = map(int, input().split())
C, D = map(int, input().split())

a, b = B, D
while b > 0:
    a, b = b, a%b

up = ((A * D) // a) + ((C * B) // a)
down = (B * D) // a

a, b = up, down
while b > 0:
    a, b = b, a%b


if a != 1:
    up /= a
    down /= a

print(int(up), int(down))
