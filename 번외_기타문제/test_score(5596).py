n = list(map(int, input().split()))
t = list(map(int, input().split()))

n_score, t_score = 0, 0

for i, j in zip(n, t):
    n_score += i
    t_score += j

if n_score >= t_score:
    print(n_score)
else:
    print(t_score)