# Time - O(Nlog N + MLogM)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    indexOne, indexTwo = 0, 0
    result = []
    smallestDifference = float("inf")
    currentDifference = float("inf")

    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):

        first = arrayOne[indexOne]
        second = arrayTwo[indexTwo
        ]
        if first == second:
            return [first, second]

        elif first < second:
            currentDifference = abs(first - second)
            indexOne += 1

        elif first > second:
            currentDifference = abs(first - second)
            indexTwo += 1

        if currentDifference < smallestDifference:
            smallestDifference = currentDifference
            result = [first, second]

    return result