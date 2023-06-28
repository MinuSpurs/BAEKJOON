while True:
    try:
        name = input()
    except EOFError:
        break

    result = ""
    for ch in name:
        if ch == 'i':
            result += 'e'
        elif ch == 'e':
            result += 'i'
        elif ch == 'I':
            result += 'E'
        elif ch == 'E':
            result += 'I'
        else:
            result += ch
    print(result)
