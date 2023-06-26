import sys

N = int(input())

tree_list = [0] * N
for i in range(N):
    tree = int(sys.stdin.readline())
    tree_list[i] = tree

sorted_tree = sorted(tree_list)

diff = [0] * (N-1)
for i in range(N-1):
    diff[i] = sorted_tree[i+1] - sorted_tree[i]

sorted_diff = sorted(diff)
gcd = sorted_tree[1] - sorted_tree[0]
for i in range(len(sorted_diff) - 1):
    a, b = sorted_diff[i+1], sorted_diff[i]
    while b > 0:
        a, b = b, a%b
    if gcd > a:
        gcd = a

i = 0
cnt = 0

for i in sorted_diff:
    cnt += (i//gcd) - 1

print(cnt)