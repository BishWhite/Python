X = "qwerty"

def func():
    print ( X )

func() # wynikiem bedzie wyraz "qwerty" ponieważ funkcja print w funkcji w tym przypadku odnosi się do zmiennej globalnej kodu.


X = "qwerty"

def func():
    X = "abc"

func()
print ( X ) # wynikiem bedzie wyraz "qwerty" ponieważ print jest poza wywołaną funkcją a przypisanie dokonane w funkcji jest lokalne


X = "qwerty"

def func():
    global X
    X = "abc"

func()
print ( X ) # wynikiem bedzie wyraz "abc" ponieważ w tym przypadku przypisanie dokonane w funkcji zmienia zmienna globalną x