a, b, c, d, e, f = map(int, input().split())
x, y = 0, 0

if a != 0 and d != 0:
    y = (d*c - f*a) / (b*d - a*e)
    x = (c - b * y) / a
elif a == 0:
    y = c/b
    x = (f - e * y) / d
elif d == 0:
    y = f/e
    x = (c - b * y) / a
    
print(int(x), int(y))