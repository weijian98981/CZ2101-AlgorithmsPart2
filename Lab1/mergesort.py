import timeit


def main():
    arr = open("number1000.txt").read().split()     # Replace test file here
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    #print(arr)
    time_start = timeit.default_timer()
    comparisons = mergesort(arr, 0, len(arr) - 1)
    time_stop = timeit.default_timer()
    print(arr)
    print("Time elapsed for program: ", (time_stop - time_start)*1000, "milliseconds")  # Time in milliseconds
    print("The total number of comparisons: ", comparisons)


def mergesort(arr, n, m):
    x = y = comparisons = 0
    mid = (n + m) // 2
    if m - n <= 0:
        return comparisons
    elif m - n > 1:
        x = mergesort(arr, n, mid)
        y = mergesort(arr, mid + 1, m)
    comparisons = merge(arr, n, m)
    return x+y+comparisons


def merge(arr, n, m):
    comparisons = 0
    if m - n <= 0:
        return comparisons

    mid = (n + m) // 2
    left = arr[n:mid + 1]
    right = arr[mid + 1:m + 1]
    while len(left) != 0 and len(right) != 0:
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
            
    return comparisons

main()
