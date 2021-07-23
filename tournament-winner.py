# Time - O (N) | Space O(N)
def tournamentWinner(competitions, results):
    points = {}

    for comp in range(len(competitions)):
        if results[comp] == 1:
            if competitions[comp][0] not in points:
                points[competitions[comp][0]] = 3
            else:
                points[competitions[comp][0]] = points[competitions[comp][0]] + 3
        else:
            if competitions[comp][1] not in points:
                points[competitions[comp][1]] = 3
            else:
                points[competitions[comp][1]] = points[competitions[comp][1]] + 3

    winner = ""
    maxPoints = -1

    for key in points:
        if points[key] > maxPoints:
            winner = key
            maxPoints = points[key]

    return winner