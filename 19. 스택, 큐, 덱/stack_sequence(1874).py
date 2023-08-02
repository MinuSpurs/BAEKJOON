import sys

n = int(input())
sequence = []
for _ in range(n):
    sequence.append(int(sys.stdin.readline()))

stack = []
answer = []
cur_num = 1

for seq_num in sequence:
    while cur_num <= seq_num:
        stack.append(cur_num)
        answer.append('+')
        cur_num += 1

    if stack[-1] == seq_num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        break
else:
    for ans in answer:
        print(ans)
