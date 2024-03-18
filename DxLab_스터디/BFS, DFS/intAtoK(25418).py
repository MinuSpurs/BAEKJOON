from collections import deque

def min_operations(a, k):
    visited = set()
    queue = deque([(a, 0)])
    while queue:
        current, count = queue.popleft()
        if current == k:
            return count
        operation = [current+1, current*2]
        for next in operation:
            if next <= k and next not in visited:
                visited.add(next)
                queue.append((next, count+1))
    return -1


a, k = map(int, input().split())
print(min_operations(a, k))