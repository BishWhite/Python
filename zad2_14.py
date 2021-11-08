line = "dakda dnca\na\nada\na"

t = line.split()
res = 0
ii = 0
for i in range(len(t)):
    if len(t[i])> res:
        res = len(t[i])
        ii = i

print(res,t[ii])
