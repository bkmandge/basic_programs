def findElement(arr, target):
    n = len(arr)  # number of elements in array
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [1, 2, 3, 4, 5, 6, 7]
target = 7

print(findElement(nums, target))
