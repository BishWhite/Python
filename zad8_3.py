import random
def calc_pi(n=100):
    

    w = 0
    for i in range(0, n):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1.0:
            w += 1
    return 4 * w / n

