def fibonacci(n):
    a=1
    b=1
    c=0
    if ((n==1)or(n==2)): 
        return 1
    
    for x in range(3,n+1):
            c=a+b
            a=b
            b=c
    return b

print(fibonacci(int(input())))