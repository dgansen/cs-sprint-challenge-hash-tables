def intersection(arrays):
    """
    YOUR CODE HERE
    """
    mem = {}
    for num in arrays[0]:
        mem[num] = 1
    
    for arr in arrays[1:]:
        for num in arr:
            if num in mem:
                mem[num] += 1
    
    return [k for k in mem if mem[k]==len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
