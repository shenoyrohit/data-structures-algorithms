# Keep pushing your dimension inward and recursively traverse the multi-dimensional array
Time: O(N) | Space: O(N)
def spiralTraverse(array):
    result = []
    startR, endR = 0, len(array) - 1
    startC, endC = 0, len(array[0]) - 1

    while startR <= endR and startC <= endC:
        for col in range(startC, endC + 1):
            result.append(array[startR][col])

        for row in range(startR + 1, endR + 1):
            result.append(array[row][endC])

        for lastCol in reversed(range(startC, endC)):
            if startR == endR:
                break
            result.append(array[endR][lastCol])

        for lastRow in reversed(range(startR + 1, endR)):
            if startC == endC:
                break
            result.append(array[lastRow][startC])

        startR += 1
        endR -= 1
        startC += 1
        endC -= 1

    return result

