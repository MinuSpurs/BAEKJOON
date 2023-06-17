import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '0':
        break
    for i in range(len(word)//2 + 1):
        if word[i] == word[len(word)-(i + 1)]:
            if i == len(word)//2:
                print('yes')
        else:
            print('no')
            break
