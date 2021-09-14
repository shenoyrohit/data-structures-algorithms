# Time: O(N) | Space: O(N)
def firstDuplicateValue(array):
    myDict = {}

    for elem in array:
        if elem in myDict.keys():
            return elem
        else:
            myDict[elem] = True
    return -1

# Time: O(N) | Space: O(1)
def firstDuplicateValueOptimized(array):
	for elem in array:
		if array[abs(elem) - 1] < 0:
			return abs(elem)
		else:
			array[abs(elem) - 1] = array[abs(elem) - 1] * -1
	return -1