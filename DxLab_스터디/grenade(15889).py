N = int(input())
N_list = list(map(int, input().split()))

if N == 1:
    print('권병장님, 중대장님이 찾으십니다')
else:
    intersection = list(map(int, input().split()))
    max_range = 0
    for i in range(N-1):
        max_range = max(max_range, N_list[i] + intersection[i])
        if max_range < N_list[i+1]:
            print('엄마 나 전역 늦어질 것 같아')
            break
    else:
        print('권병장님, 중대장님이 찾으십니다')