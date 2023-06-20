a, b = map(int, input().split())

i = min(a,b)
factor, multiple = 0, 0

while True:
    if a % i == 0 and b % i == 0:
        factor = i
        break
    else:
        i -= 1

multiple = int((a * b) / factor)

print(factor)
print(multiple)