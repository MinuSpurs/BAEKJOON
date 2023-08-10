import math

N = int(input())

tree_list = [0] * N
for i in range(N):
    tree = int(input())
    tree_list[i] = tree

sorted_tree = sorted(tree_list)

diff = [0] * (N - 1)
for i in range(N - 1):
    diff[i] = sorted_tree[i + 1] - sorted_tree[i]

gcd = diff[0]
for i in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[i])

cnt = 0
for i in diff:
    cnt += (i // gcd) - 1

print(cnt)