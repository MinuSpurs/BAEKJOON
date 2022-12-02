N = int(input())
score,ans = [], []

for i in range(N):
    ans.append(input())

for i in range(N):
    score_num = 0
    total = 0
    for j in range(len(ans[i])):
        if ans[i][j] == 'O':
            score_num+=1
            total+=score_num
        else:
            score_num = 0
    score.append(total)

for i in range(N):
    print(score[i])