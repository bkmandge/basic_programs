def searchInsert(arr, target):
    n = len(arr)

    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            ans = mid
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans


nums = [1, 3, 5, 6]
# target = 7
target = 2
print(searchInsert(nums, target))
