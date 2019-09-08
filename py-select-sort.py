# select sort algorithm
def findSmallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1 - len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

