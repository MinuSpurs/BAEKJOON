def solve(a: list) -> int:
    print(type(a))
    result = 0
    for i in range(len(a)):
        result += a[i]
    return result

a = [1,2,3,4,5]
good = solve(a)
print(good)