def search(L1,L2):
    s1 = set(L1)
    s2 = set(L2)
    print(s1.intersection(s2),s1.union(s2))
    
   

search(["ag","b","c","d",1,6,55,10,10,10],["a","b",7,9,6,10,10,"d"])