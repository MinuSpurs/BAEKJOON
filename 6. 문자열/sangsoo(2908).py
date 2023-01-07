A, B = map(int,input().split())

A1 = (A // 100) + (((A % 100) // 10) * 10) + ((A % 10) * 100)
B1 = (B // 100) + (((B % 100) // 10) * 10) + ((B % 10) * 100)

if A1 > B1:
    print(A1)
else:
    print(B1)