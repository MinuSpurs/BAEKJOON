import sys

def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid = len(unsorted_list) //2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    i, j = 0,0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            sorted_list.append(left[i])
            i += 1
        elif left[i][0] == right[j][0]:
            if left[i][1] < right[j][1]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

N = int(input())
unsorted_list = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    unsorted_list.append(temp)

coor = merge_sort(unsorted_list)

for i in range(len(coor)):
    print(coor[i][0], coor[i][1])