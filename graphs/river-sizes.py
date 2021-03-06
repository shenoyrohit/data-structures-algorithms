# Time: O (wh or N - where N is total elements) | Space: O (wh)
def riverSizes(matrix):
    # initialize sizes results array and a visited counter
    sizes = []
    visited = [[False for spot in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] == True:
                continue
            # if unvisited, traverse node
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

# DFS helper function - iterative
def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0

    # iterative DFS (initialize stack) and add initial node
    nodesToExplore = [[i, j]]
    while len(nodesToExplore) > 0:
        currentNode = nodesToExplore.pop()

        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j]:
            continue

        # Mark node as visited - prevents duplicates & iterative DFS duplicates
        visited[i][j] = True

        if matrix[i][j] == 0:
            continue

        # add to current river size
        currentRiverSize += 1

        # get neighbors of current node
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)

        # Append neighbors to the stack - explore DFS iteratively
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    # If river found, append to results
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])

    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])

    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])

    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])

    return unvisitedNeighbors