# Time: O (N) | Space: O(1)
def hasSingleCycle(array):
    STARTING_IDX = 0

    numElementsVisited = 0
    currentIdx = STARTING_IDX

    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == STARTING_IDX:
            return False
        numElementsVisited += 1
        currentIdx = getNextIndex(currentIdx, array)
    return currentIdx == STARTING_IDX


def getNextIndex(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)