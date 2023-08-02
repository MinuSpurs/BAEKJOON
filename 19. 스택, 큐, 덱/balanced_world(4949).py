import sys

while True:
    word = sys.stdin.readline().rstrip()
    ps_list = []
    if word == '.':
        break
    for i in range(len(word)):
        if word[i] == '.':
            break
        elif len(ps_list) == 0 and (word[i] == ']' or word[i] == ')'):
            ps_list.append(word[i])
            break
        elif word[i] == '(' or word[i] == '[':
            ps_list.append(word[i])
        elif word[i] == ')' and ps_list[-1] == '(':
            ps_list.pop()
        elif word[i] == ')' and ps_list[-1] != '(':
            break
        elif word[i] == ']' and ps_list[-1] == '[':
            ps_list.pop()
        elif word[i] == ']' and ps_list[-1] != '[':
            break
    print('yes' if len(ps_list) == 0 else 'no')