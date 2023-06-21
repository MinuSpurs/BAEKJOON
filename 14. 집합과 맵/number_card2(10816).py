import sys

N = int(input())
my_card = tuple(map(int, sys.stdin.readline().split()))

M = int(input())
card_list = tuple(map(int, sys.stdin.readline().split()))

card_dict = {}
result = [0] * M

for i in my_card:
    if i in card_dict.keys():
        card_dict[i] += 1
    else:
        card_dict[i] = 1

for i in range(len(card_list)):
    if card_list[i] in card_dict.keys():
        result[i] = card_dict[card_list[i]]
    else:
        result[i] = 0

print(* result)