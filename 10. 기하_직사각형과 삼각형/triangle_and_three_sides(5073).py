while True:
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)

    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    elif a[1] + a[2] <= a[0]:
        print('Invalid')
        continue
    elif a[0] == a[1] and a[1] == a[2] and a[0] == a[2]:
        print('Equilateral')
        continue
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        print('Isosceles')
        continue
    elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
        print('Scalene')
        continue