while True:
    try:
        line = input()
        if not line:  # 만약 빈 줄이면 종료
            break
        print(line)
    except EOFError:
        break
