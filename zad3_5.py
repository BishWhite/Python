line = "|"
s = line
n = int(input())
for i in range(n):
    s = s + "....|"

s=s+"\n"+"0"


for j in range(1,n+1):
    s1= str(j)
    s1= s1.rjust(5)
    s= s + s1


print(s)