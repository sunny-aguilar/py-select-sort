# select sort algorithm
def main():
    print()

# returns the index of the smallest value in an array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1 - len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort():
    new_array = []



