# select sort algorithm
def main():
    array = [34, 12, 10, 3, 8, 2, 9, 1, 32, 22, 15, 14]
    select_sort(array)

# returns the index of the smallest value in an array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1 - len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array

