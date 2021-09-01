import timeit

def main():
    arr = open("ascending10000.txt").read().split()  # Replace test file here
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    print(arr)
#     arr = [14,40,31,28,3,15,17,51]
    time_start = timeit.default_timer()
    comparisons = mergesort(arr, 0, len(arr) - 1)
    time_stop = timeit.default_timer()
    #print(arr)
    print("Time elapsed for program: ", (time_stop - time_start) * 1000, "milliseconds")  # Time in milliseconds
    print("Number of comparisons: ", comparisons)


def mergesort(arr, n, m):
    x = y = z = comparisons = 0
    mid = (n + m) // 2
    if m - n < 42:  # insert S here
        z = insertionSort(arr, n, m)  # code here is changed to perform insertion sort below S elements
    elif m - n >= 42:  # insert S here
        x = mergesort(arr, n, mid)
        y = mergesort(arr, mid + 1, m)
        comparisons = merge(arr, n, m)

    return comparisons+x+y+z


def merge(arr, n, m):
    comparisons = 0
    
    if m - n <= 0:
        return 1
    
    mid = (n + m) // 2
    left = arr[n:mid + 1]
    right = arr[mid + 1:m + 1]
    did = False
    
    while len(left) != 0 and len(right) != 0:
        did = True
        comparisons+=1
        if left[0] < right[0]:
            arr[n] = left[0]
            left.pop(0)
        elif left[0] > right[0]:
            arr[n] = right[0]
            right.pop(0)
        elif left[0] == right[0]:
            arr[n] = left[0]
            n += 1
            arr[n] = right[0]
            left.pop(0)
            right.pop(0)
        n += 1

    if len(left) != 0:
        while len(left) != 0:
            arr[n] = left[0]
            left.pop(0)
            n += 1
    elif len(right) != 0:
        while len(right) != 0:
            arr[n] = right[0]
            right.pop(0)
            n += 1
    
    if did == False:
        comparisons+=1
        
    return comparisons


def insertionSort(arr, n, m):
    comparisons = 0
    for i in range(n, m + 1):
        key = arr[i]
        j = i - 1
        did = False
        while j >= n and key < arr[j]:
            did = True
            comparisons+=1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        if did == False:
            comparisons+=1

    return comparisons


main()
