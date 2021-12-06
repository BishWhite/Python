import math

def heron(a, b, c):
    

    p = (a + b + c) / 2
    if not (a < b+c and b < a+c and c < a+b):
        raise ValueError('Niepoprawne dane wejsciowe')

    return math.sqrt(p*(p-a)*(p-b)*(p-c))