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
        if int(left[i][0]) < int(right[j][0]):
            sorted_list.append(left[i])
            i += 1
        elif int(left[i][0]) == int(right[j][0]):
            sorted_list.append(left[i])
            i += 1
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
    value = list(sys.stdin.readline().split())
    unsorted_list.append(value)

sorted_list = merge_sort(unsorted_list)

for i in range(len(sorted_list)):
    print(int(sorted_list[i][0]), sorted_list[i][1])