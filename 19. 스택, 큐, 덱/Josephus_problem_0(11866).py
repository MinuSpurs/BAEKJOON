from collections import deque

n, k = map(int, input().split())

queue = deque([i + 1 for i in range(n)])
jose = []

while queue:  # queue에 원소가 남아있는 동안 반복
    for _ in range(k - 1):  # k-1번째 요소를 처리하기 위한 위치 변경
        queue.append(queue.popleft())
    
    jose.append(queue.popleft())  # 요세푸스 순열에 선택된 원소 추가

print("<" + ", ".join(map(str, jose)) + ">")  # 출력 양식에 맞게 출력
