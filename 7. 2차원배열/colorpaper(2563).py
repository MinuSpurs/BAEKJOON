paper = [[0] * 100 for _ in range(100)]  # 100x100 크기의 흰색 도화지 배열 초기화

print(paper)
"""
n = int(input())  # 색종이의 수

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1  # 검은색 색종이가 있는 부분을 1로 설정

area = 0  # 검은 영역의 넓이

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1  # 1로 설정된 영역을 세어 넓이를 증가시킴

print(area)
"""