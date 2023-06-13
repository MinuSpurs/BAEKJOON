import sys

N, k = map(int, input().split())

score = list(map(int, sys.stdin.readline().split()))

for i in range(N-1, 0, -1):
    for j in range(i):
        if score[j] < score[j+1]:
            temp = score[j]
            score[j] = score[j+1]
            score[j+1] = temp

print(score)
print(score[k-1])