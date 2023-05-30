N, B = map(int, input().split())

result = ''

while N > 0:
    N, mod = divmod(N, B)
    if mod >= 10:
        mod = chr(mod + 55)     
        result += mod
    else:
        result += str(mod)

result = result[::-1]
print(result)