

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while(left <= right):
        m = left + (right - left) // 2
        mid = arr[m]
        print(m)

        if mid == target:
            return (mid, m)
        if target > mid:
            left = m+1
        else:
            right = m-1
    return "not found"

import time
arr = [1,2,3,4,5,7,8,50]
target = 5

print(len(arr))
print(binary_search(arr, target))