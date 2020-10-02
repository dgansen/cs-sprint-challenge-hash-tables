def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    d = {}
    for i,w in enumerate(weights):
        gap = limit-w
        if gap in d:
            return (i, d[gap])
        d[w] = i

    return None
