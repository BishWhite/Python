def make_ruler(n):
    line = "|"
    s = line
    for i in range(n):
        s = s + "....|"

    s=s+"\n"+"0"


    for j in range(1,n+1):
        s1= str(j)
        s1= s1.rjust(5)
        s= s + s1

    return s





def make_grid(rows, cols):
    line = "|"
    line1 = "+"
    s = ""

    for i in range(cols):
        line = line + " "*3 + "|"
        line1 = line1 + "---+"


    for i in range(2*rows+1):
        if i%2==0:
            s = s + line1
        else:
            s = s + line

        if i < 2*rows:
            s = s + "\n"    

    return s



print(make_ruler(7))
print(make_grid(3,4))
    