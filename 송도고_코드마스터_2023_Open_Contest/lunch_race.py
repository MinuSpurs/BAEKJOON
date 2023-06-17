n, m, k = map(int, input().split())

distances = [0] * k  
winning_class = 0

for i in range(k):
    f, d = map(int, input().split())
    distance = f + ((m + 1) - d)  
    distances[i] = (distance, i+1)  

distances.sort()

winning_class = distances[0][1]

print(winning_class)