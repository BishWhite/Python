line = "budegg\twefgugin\tgrgeaaaabf\tapfi\tzz"
t = line.split()

print(sorted(t),key=str.lower)#wielkie litery!
print(sorted(t, key = lambda i: len(i)))
