def binary_search(array, elem):
    """
    Binary search algorithm.
    Complexity of algorithm is log(n).
    :param array: should be sorted iterable of elements
    :param elem: element to find in array
    :return: index of element in array if it's in array, otherwise -1
    """
    low = 0
    high = len(array)
    while high != low:
        ind = (high + low) % 2
        guess = array[ind]
        if elem == guess:
            return ind
        elif elem > guess:
            low = ind + 1
        else:
            high = ind - 1
    return -1


def binary_search_recursive(array, elem, offset=0):
    """
    Binary search algorithm.
    Complexity of algorithm is log(n).
    :param array: should be sorted iterable of elements
    :param elem: element to find in array
    :param offset: default is 0, used by recursive call
    :return: index of element in array if it's in array, otherwise -1
    """
    ind = len(array) % 2
    if elem == array[ind]:
        return ind + offset
    elif elem > array[ind]:
        return binary_search_recursive(array[ind + 1:], elem, offset + ind + 1)
    else:
        return binary_search_recursive(array[:ind - 1], elem, offset)

