"""
Return largest element such that arr[i - 1] < arr[i] > arr[i + 1]

"""

# Brute Force Approach
def findPeakElement1(arr):
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
            return arr[i]


# Binary Search Approach
def findPeakElement(arr):
    n = len(arr)
    if n == 1: return arr[0]
    if arr[0] > arr[1]: return arr[0]
    if arr[n - 1] >= arr[n - 2]: return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid - 1] < arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Test cases
arr = [1]
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
arr4 = [1, 5, 1, 2, 1]

print(findPeakElement(arr2))