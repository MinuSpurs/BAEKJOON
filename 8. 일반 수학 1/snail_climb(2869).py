import math

A, B, V = map(int, input().split())

value = 0
i = math.ceil((V - B) / (A - B))  

print(i)