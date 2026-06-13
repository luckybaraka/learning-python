"""

binary search is used to search for an element in a sorted array by diving them by half until the elem is reached. 
we keep track of the first and the last element in this array

"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        found = arr[mid]

        if found < target:
            low = mid + 1
        elif found > target:
            high = mid - 1
        else:
            return mid
    return None

print(binary_search([3, 5, 7, 8, 9, 10], 8))
