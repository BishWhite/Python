line = "dakda dnca\na\nada\na"

t=line.split()

res = 0
for i in t:
    res += len(i)

print(res)