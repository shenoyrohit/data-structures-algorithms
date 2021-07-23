# Input - array, subsequence
# Output - True/False
# Not adjacent, but appears in same order

# Time - O(N) | Space - O(1)
def isValidSubsequence(array, sequence):
    currIndex = 0
    sequenceIndex = 0

    while currIndex < len(array) and sequenceIndex < len(sequence):
        if array[currIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        currIndex += 1

    return sequenceIndex == len(sequence)
