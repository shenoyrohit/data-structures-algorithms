# Input - Array of distinct integers
# Input - Target integer sum
# Returns - Array of two nums matching sum, else empty array
# Sum only two different integers
# At most one pair of numbers summing to target sum

# Brute force - O(N^2) Time | O(1) Space
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		for j in range(i + 1, len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
	return []


# HashMap - O(N) Time | O(N) Space
def twoNumberSumHash(array, targetSum):
    myMap = {}

    # iterate array
    for i in range(len(array)):
        # find counterpart
        potentialNum = targetSum - array[i]
        if potentialNum in myMap:
            return [array[i], targetSum - array[i]]

        myMap[array[i]] = True


# LR Pointers - O(NlogN) Time | O(1) Space
def twoNumberSumPointer(array, targetSum):
    left = 0
    right = len(array) - 1

    array.sort()

    while (left < right):
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return []