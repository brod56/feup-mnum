# All methods suppose a single local minima exists

import math

def min_simple_search(f, x, h):
    right = f(x + h) < f(x)
    while True:
        nx = x + h if right else x-h
        if f(nx) >= f(x): return x
        x = nx


def min_trisection(f, a, d, tolerance):
    count = 0
    while d - a > tolerance:
        count += 1
        b = a + (d-a)/3
        c = d - (d-a)/3
        if f(b) > f(c):
            a = b
        else:
            d = c
    return (d+a)/2, count


def min_aurea(f, a, d, tolerance):
    K = (math.sqrt(5) - 1) / 2
    b = d - (d - a) * K
    c = a + (d - a) * K
    fc = f(c)
    fb = f(b)
    count = 0
    while d - a > tolerance:
        count += 1
        if fb > fc:
            a = b
            b = c
            fb = fc
            c = a + (d - a) * K
            fc = f(c)
        else:
            d = c
            c = b
            fc = fb
            b = d - (d - a) * K
            fb = f(b)
    return (d+a)/2, count

if __name__ == '__main__':
    f = lambda x: (x+2)**2 - 5
    print(min_simple_search(f, -5, 0.00001))
    print(min_trisection(f, -5, 5, 0.00001))
    print(min_aurea(f, -5, 5, 0.001))