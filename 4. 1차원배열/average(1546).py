N = int(input())
score = list(map(int, input().split()))
best_score = max(score)
avr = 0

for i in range(N):
    score[i] = (score[i]/best_score)*100

for i in range(N):
    avr += score[i]
avr = avr/N
print(avr)