# Time Complexity: N
# Space Complexity: O(1)
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        # element to move found - swap
        if array[left] == toMove and array[left] != array[right]:
            # swap
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

            # increment pointers
            left += 1
            right -= 1
        else:
            # don't swap, move left pointer to next
            left += 1

    return array