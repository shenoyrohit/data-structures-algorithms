# Time: O (N ^ 2) | Space: O(N)
def arrayOfProducts(array):
    output = []

    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i != j:
                product = product * array[j]
        output.append(product)
    return output


# Time: O(N) | Space: O(N)
def arrayOfProductsN(array):
    left = [1 for i in range(len(array))]
    right = [1 for i in range(len(array))]
    output = [1 for i in range(len(array))]

    prodL = 1
    prodR = 1
    idx = len(array) - 1

    # Make left product array
    for i in range(len(array)):
        left[i] = prodL
        prodL = prodL * array[i]

    # Make right product array
    while idx >= 0:
        right[idx] = prodR
        prodR = prodR * array[idx]
        idx -= 1

    # Merge
    for i in range(len(array)):
        output[i] = left[i] * right[i]

    return output
