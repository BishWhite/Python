line = "budegg\twefgugin\tgrgeaaaabf\tapfi\tzz"
t = line.split()

print(sorted(t))
print(sorted(t, key = lambda i: len(i)))
