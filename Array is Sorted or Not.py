# Brute Force Approach:- O(N2)
def isSorted(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i + 1]:
                return True
    return False


arr = [1, 5, 4, 3, 2]
# print(isSorted(arr))


# Optimal Approach:- O(N)

def isSorted2(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            # elements where condition fails
            # print(arr[i])
            # print(arr[i - 1])
            return i
    return 0


arr1 = [1, 2, 3, 4, 0, 5]
print(isSorted2(arr1))
