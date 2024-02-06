def countElement(arr, target):
    n = len(arr)

    low = 0
    high = n - 1

    first = -1
    last = -1
    count = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if first == -1 and last == -1:
        return count

    count = last - first + 1
    return count


nums = [2, 4, 10, 10, 10, 18, 20]
target = 25
print(countElement(nums, target))
