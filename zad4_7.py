def flatten(sequence):
    if not isinstance(sequence, (list, tuple)):
        return -1

    L = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            L.extend(flatten(x))
        else:
            L.append(x)
    return L

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print ( flatten(seq) )