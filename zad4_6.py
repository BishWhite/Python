def sum_seq(sequence):
    if not isinstance(sequence, (list, tuple)):
        return -1

    s = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            s += sum_seq(x)
        else:
            s += x
    return s


seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(sum_seq(seq))