import sys

n = int(input())
num_dict = {}
num_list = [0] * n
cnt = 0

for i in range(n):
    num = int(sys.stdin.readline())
    num_list[i] = num
    cnt += num
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

num_dict = dict(sorted(num_dict.items()))
num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
num_list = sorted(num_list)

print(round(cnt / n))
print(num_list[n // 2])
if len(num_dict) > 1:
    if num_dict[0][1] == num_dict[1][1]:
        print(num_dict[1][0])
    else:
        print(num_dict[0][0])
else:
    print(num_dict[0][0])
print(num_list[-1] - num_list[0])