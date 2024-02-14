import sys

N = int(input())
unsorted_list = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(set(unsorted_list))
index_dict = {num: i for i, num in enumerate(sorted_list)}


result = [index_dict[num] for num in unsorted_list]

for i in result:
    print(i, end=' ')