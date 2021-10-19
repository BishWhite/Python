L = [121, 10, 1, 101, 1, 99, 91, 66, 5, 54]
s = ""
for i in L:
    t = str(i)
    s += t.zfill(3) + " "


print(s[:-1])
# " ".join(str(x).zfill(3) for x in L)
# 
