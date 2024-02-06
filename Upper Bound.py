# Upper Bound:- Last occurrence of number

def upperBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


nums = [1, 2, 3, 3, 4, 5, 6, 7]
target = 3

print(upperBound(nums, target))

