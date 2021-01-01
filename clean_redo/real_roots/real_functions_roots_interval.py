import math


def bissection_absolute_precision(f, a, b, error):
    if f(a) * f(b) >= 0:
        print("wrong interval guess")
        return
    while abs(a - b) > error:
        xn = (a + b) / 2
        if f(a) * f(xn) < 0:  # left interval contains the root
            b = xn
        else:
            a = xn
    return (a + b) / 2


def false_position_null_at_root(f, a, b, error):
    if f(a) * f(b) >= 0:
        print("wrong interval guess")
        return
    while abs(f(a) - f(b)) > error:
        xn = (f(b) * a - f(a) * b) / (f(b) - f(a))
        if f(a) * f(xn) < 0:  # left interval contains the root
            b = xn
        else:
            a = xn
    return (a + b) / 2


def false_position_max_iterations(f, a, b, max_iterations):
    if f(a) * f(b) >= 0:
        print("wrong interval guess")
        return
    for i in range(max_iterations):
        xn = (f(b) * a - f(a) * b) / (f(b) - f(a))
        if f(a) * f(xn) < 0:  # left interval contains the root
            b = xn
        else:
            a = xn
    return (a + b) / 2
