# Time-O(N^3), Space = O(N)
def threeNumberSum(array, targetSum):
    triplets = []

    for one in range(len(array) - 2):
        for two in range(one + 1, len(array) - 1):
            for three in range(two + 1, len(array)):
                currentSum = array[one] + array[two] + array[three]
                if targetSum == currentSum:
                    trip = [array[one], array[two], array[three]]
                    trip.sort()
                    triplets.append(trip)

    triplets.sort()
    return triplets


# O (N^2 Time) | O (N) space
def threeNumberSumSorted(array, targetSum):
    array.sort()

    triplets = []

    for ind in range(len(array) - 2):
        left = ind + 1
        right = len(array) - 1

        while left < right:
            currentSum = array[ind] + array[left] + array[right]

            if currentSum == targetSum:
                trip = [array[ind], array[left], array[right]]
                trip.sort()

                triplets.append(trip)
                left += 1
                right -= 1

            elif currentSum < targetSum:
                left += 1

            else:
                right -= 1

    triplets.sort()

    return triplets