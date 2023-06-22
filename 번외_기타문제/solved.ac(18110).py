import sys

def score_round(cnt):
    if cnt - int(cnt) >= 0.5:
        return int(cnt) + 1
    else:
        return int(cnt)

n = int(input())

if n == 0:
    print(0)
else:
    cnt = n * 0.15
    score_list = [0] * 31

    cnt = score_round(cnt)
    sorted_score = [0] * n

    for i in range(n):
        num = int(sys.stdin.readline())
        score_list[num] += 1

    list_cnt = 0
    for i in range(31):
        if score_list[i] != 0:
            for j in range(score_list[i]):
                sorted_score[list_cnt] = i
                list_cnt += 1

    result = 0
    i = 0

    while i < n:
        if i < cnt or (n - i - 1) < cnt:
            i += 1
        else:
            result += sorted_score[i]
            i += 1


    print(score_round(result/(n - (2 * cnt))))