n= int(input())
k = int(input())
line = "|"
line1 = "+"
s = ""

for i in range(k):
    line = line + " "*3 + "|"
    line1 = line1 + "---+"


for i in range(2*n+1):
    if i%2==0:
        s = s + line1
    else:
        s = s + line

    if i < 2*n:
        s = s + "\n"    


print(s)