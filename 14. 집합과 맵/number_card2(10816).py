import sys

N = int(input())
my_card = tuple(map(int, sys.stdin.readline().split()))

M = int(input())
card_list = tuple(map(int, sys.stdin.readline().split()))

dict = {}

for i in range(len(card_list)):
    dict[card_list[i]] = 0

for i in range (len(my_card)):
    if my_card[i] in dict.keys():
        dict[my_card[i]] += 1

print(* dict.values())