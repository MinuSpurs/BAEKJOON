s = int(input())
s_list = list(map( int, input().split()))

real = []


for i in range(s):
    real.insert(s_list[i], i+1)

real.reverse()

print(*real)