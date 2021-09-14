'''
Initialize a counter to keep track of current longest peak - start at -inf
Traverse the array once - left to right
Iterate through triplets (minimum req for a peak) and check every triplet for a peak
Peak is when 2nd  > 1st and 2nd < 3rd
Once a peak is found, traverse both ways from the peak to find it's length
Check against currentLongest peak and keep count
'''


# Time: O(N) | Space: O(1)
def longestPeak(array):
    currentLongest = 0
    idx = 1
    isCurrentPeak = False

    while idx < len(array) - 1:
        isCurrentPeak = isAPeak(array[idx - 1], array[idx], array[idx + 1])

        if not isCurrentPeak:
            idx += 1
            continue

        leftIdx = idx - 2
        rightIdx = idx + 2

        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeak = rightIdx - leftIdx - 1
        currentLongest = max(currentPeak, currentLongest)

        idx = rightIdx

    return currentLongest


def isAPeak(left, center, right):
    if center > left and center > right:
        return True
    else:
        return False

