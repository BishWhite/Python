def push(s,D):
    n=len(s)
    result = 0
    tmp = 0
    current = 0
    for i in range(n):
        current = D[s[i]]
        if i < n - 1:
            tmp = D[s[i+1]]
            if tmp> current:
                current=-current    
        result+=current
    D[s]=result



R= ["I", "V", "X", "L", "C", "D", "M"]
A= [1,5,10,50,100,500,1000 ]
D = dict(zip(R, A))
D1={}
for (k,v) in zip(R,A):
    D1[k]=v

s= input()
push(s,D)
push(s,D1)
print(D[s])
print(D1[s])