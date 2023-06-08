a = list(map(int, input().split()))

a = sorted(a, reverse=True)

if a[0] >= a[1] + a[2]:
    a[0] = a[1] + a[2] - 1

print(a[0] + a[1] + a[2])