# Time: O(N) | Space: O(N)
def firstDuplicateValue(array):
    myDict = {}

    for elem in array:
        if elem in myDict.keys():
            return elem
        else:
            myDict[elem] = True
    return -1