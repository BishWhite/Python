def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        print("równanie posiada nieskonczenie wiele rozwiazań")
    elif a == 0 and b == 0 and c!=0:
        print('równanie sprzeczne')
    elif b == 0:
        print("prosta równoległa do osi OY, przecina oś OX w punkcie x = -c/a =", -c/a)
    elif a == 0:
        print("prosta równoległa do osi OX, przecina oś OY w punkcie y = -c/b =", -c/b)
        
    else:  
        print("prosta przecina oś OX w punkcie x = ", -c/a)
        print("prosta przecina oś OY w punkcie y = ", -c/b)

    if c == 0 and not (a == 0 and b == 0):
        print("prosta przechodzi przez początek układu współrzędnych")



