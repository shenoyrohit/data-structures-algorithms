# Time: O(N logN) | Space: O(N)
def sortedSquaredArray(array):
    squared = []
    for index in range(len(array)):
        squared.append(array[index] * array[index])


    squared.sort()

    return squared


# Time: O(N) | Space: O(N)
def sortedSquaredArrayLinear(array):
    squared = [0 for _ in array]

    left = 0
    right = len(array) - 1

    for ind in reversed(range(len(array))):
        small = array[left]
        large = array[right]

        if abs(small) > abs(right):
            squared[ind] = small * small
            left += 1
        else:
            squared[ind] = large * large
            right -= 1

    return squared

