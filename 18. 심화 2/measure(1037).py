s = int(input())
s_list = list(map(int, input().split()))

if s % 2 == 0:
    print(max(s_list) * min(s_list))
else:
    print(sorted(s_list)[(s // 2)] ** 2)