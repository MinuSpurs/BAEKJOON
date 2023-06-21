N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

first = len(A-B)
second = len(B-A)

print(first + second)