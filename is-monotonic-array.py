# Input - array of integers
# Returns - boolean

# Time: O (N) | Space: O(1)
def isMonotonic(array):
    if len(array) < 2:
        return True

    idx = 0
    increasing = False
    isMonotonic = True

    while array[idx] == array[idx + 1]:
        if idx == len(array):
            return True
        idx += 1

    if array[idx] > array[idx + 1]:
        increasing = False
    else:
        increasing = True

    for ind in range(idx, len(array) - 1):
        # non-increasing
        if increasing == False:
            if array[ind] < array[ind + 1]:
                isMonotonic = False
        # non-decreasing
        elif increasing == True:
            if array[ind] > array[ind + 1]:
                isMonotonic = False

    return isMonotonic


# Time Complexity: O(N), Space Complexity: O(1)
def isMonotonicAssumption(array):
    if len(array) < 2:
        return True

    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            isNonDecreasing = False
        if array[i] < array[i - 1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing

