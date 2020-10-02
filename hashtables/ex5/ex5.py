# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """    
    mem = {}
    for f in files:
        end = f.split('/')[-1]
        if end in mem:
            mem[end].append(f)
        else:
            mem[end] = [f]
    result = [mem[q] for q in queries if q in mem]
    
    def flatten(A):
        rt = []
        for i in A:
            if isinstance(i,list): rt.extend(flatten(i))
            else: rt.append(i)
        return rt
    return flatten(result)


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/lib/bre/new/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
