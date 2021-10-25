 
s = input()
while s!="stop":
    if not s.isnumeric():
        print("Błąd")
        s = input()
    else:
        print(s)
        k = float (s)
        print(k**3)
        s = input()