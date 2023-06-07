import sys

temp = []
angle = 0

for i in range(3):
    n = int(sys.stdin.readline())
    temp.append(n)
    angle += n

if angle == 180 and temp[0] == temp[1] and temp[1] == temp[2]:
    print('Equilateral')
elif angle == 180 and temp[0] == temp[1] or temp[1] == temp[2] or temp[0] == temp[2]:
    print('Isosceles')
elif angle == 180 and temp[0] != temp[1] and temp[1] != temp[2] and temp[0] != temp[2]:
    print('Scalene')
else:
    print('Error')