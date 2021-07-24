# Time: O (NlogN) | Space: O(1) - sort inplace
def nonConstructibleChange(coins):
    # sort input coins array
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1