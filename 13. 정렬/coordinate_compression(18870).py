import sys

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2
    left = merge_sort(unsorted_list[:mid])
    right = merge_sort(unsorted_list[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    left_length, right_length = len(left), len(right)
    
    while i < left_length and j < right_length:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

N = int(input())
unsorted_list = list(map(int, sys.stdin.readline().split()))

sorted_list = set(merge_sort(unsorted_list))


print(merge_sort(unsorted_list))
print(sorted_list)

index_dict = {num: i for i, num in enumerate(sorted_list)}

result = [index_dict[num] for num in unsorted_list]

for i in result:
    print(i, end=' ')
