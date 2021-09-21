# O (wh) Time | O (wh) Space
def removeIslands(matrix):
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isBorder(i, j, matrix):
                continue

            if matrix[i][j] != 1:
                continue

            findOnesConnectedToBorder(i, j, matrix, onesConnectedToBorder)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBorder[row][col]:
                continue

            matrix[row][col] = 0

    return matrix


def findOnesConnectedToBorder(startRow, startCol, matrix, onesConnectedToBorder):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentRow, currentCol = stack.pop()

        if onesConnectedToBorder[currentRow][currentCol]:
            continue

        onesConnectedToBorder[currentRow][currentCol] = True

        neighbors = getNeighbors(currentRow, currentCol, matrix)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)


def getNeighbors(row, col, matrix):
    neighbors = []

    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(matrix):
        neighbors.append((row + 1, col))
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(matrix[0]):
        neighbors.append((row, col + 1))

    return neighbors


def isBorder(i, j, matrix):
    rowBorder = i == 0 or i == len(matrix) - 1
    colBorder = j == 0 or j == len(matrix[i]) - 1
    isBorder = rowBorder or colBorder
    return isBorder