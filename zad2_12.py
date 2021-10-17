line = "dakdadnca\na\nada\na"
t = line.split()
print(t)
res = ""
res1 = ""
for e in t:
    res += e[0]
    res1 += e[-1]
    
print(res,res1)

