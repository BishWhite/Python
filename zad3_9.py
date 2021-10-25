def f(L):
    o=[]
    for e in L:
        o.append(sum(e))

    return o

print(f([[],[4],(1,2),[3,4],(5,6,7)]))