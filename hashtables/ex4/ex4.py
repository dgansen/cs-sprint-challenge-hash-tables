def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    result = []
    for elem in a:
        if elem not in d:
            d[elem*-1] = elem
        else:
            pos = elem if elem > 0 else d[elem]
            if pos not in result:
                result.append(pos)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
