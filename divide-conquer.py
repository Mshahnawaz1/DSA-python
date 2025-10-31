

def mergesort(arr):
    
    if len(arr) == 1:
        return arr

    h = len(arr) // 2
    left = mergesort(arr[:h])
    right = mergesort(arr[h:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [4,6,7,1,8,10,4]
print(mergesort(arr))

