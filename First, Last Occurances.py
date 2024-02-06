def firstLastOccurances(arr, target):
    n = len(arr)

    first = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    last = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return [first, last]


nums = [1, 2, 3, 3, 3, 5, 6, 7, 10]
target = 3

print(firstLastOccurances(nums, target))
