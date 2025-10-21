
# It has TO(n2) SO(1), equal elements gets swapped
def selection_sort(arr : list):
    for i, x in enumerate(arr):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

# It has TO(n2) SO(1), equal elements does not get swapped
def bubble_sort(arr: list):
    swapped = False 
    for i in range(len(arr) - 1):
        for j in range(len(arr)- 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr: list):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1 
        while( j >=0 and arr[j] > key):
            arr[j+1] = arr[j]
            steps.append(arr.copy())
            
            j-=1
        arr[j+1] = key
        steps.append(arr.copy())
    return (arr, steps)




arr = [4,6,7,1,8,10,4]
print(insertion_sort(arr))

ar, steps = insertion_sort(arr)
print(steps)