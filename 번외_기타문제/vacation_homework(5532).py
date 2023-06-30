L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

lang, math = 0, 0

if A % C != 0:
    lang = (A // C) + 1
else:
    lang = (A // C)
if B % D != 0:
    math = (B // D) + 1
else:
    math = (B // D)

print(L - max(lang, math))