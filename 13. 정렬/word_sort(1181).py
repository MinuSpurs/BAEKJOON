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
        if len(left[i]) < len(right[j]):
            sorted_list.append(left[i])
            i += 1
        elif len(left[i]) == len(right[j]):
            if left[i] < right[j]:
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
result = []

for i in range(N):
    num = sys.stdin.readline().rstrip()
    unsorted_list.append(num)

sorted_list = merge_sort(unsorted_list)

for value in sorted_list:
    if value not in result:
        result.append(value)

for i in range(len(result)):
    print(result[i])