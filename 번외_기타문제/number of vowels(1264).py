import sys

word = ''
i, cnt = 0, 0
while True:
    word = sys.stdin.readline().rstrip()
    if word == '#':
        break
    while True:
        if i + 1 >= len(word):
            print(cnt)
            i = 0
            cnt = 0
            break
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U':
            cnt += 1
        i += 1
