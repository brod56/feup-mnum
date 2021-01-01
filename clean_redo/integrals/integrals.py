def trapezoidal(f,a,b,n): # 2 ordem
    h = (b-a)/n
    return h/2 * (f(a) + f(b) + 2*sum(f(a+i*h) for i in range(1,n)))

def simpson(f,a,b,n): # 4 ordem
    h = (b-a)/n
    return h/3 * (f(a) + f(b) + sum(4*f(a+i*h)
        if i % 2 != 0 else 2*f(a+i*h) for i in range(1,n)))

def qc_trapezoidal(f,a,b,n):
    # aceitar se qc = 2^ordem = 4
    tries = []
    for i in range (3):
        tries.append(trapezoidal(f,a,b,n*(2**i)))
    return (tries[1] - tries[0]) / (tries[2] - tries[1])

def error_trapezoidal(f,a,b,n):
    tries = []
    for i in range (3):
        tries.append(trapezoidal(f,a,b,n*(2**i)))
    return (tries[2] - tries[1]) / (2**2 - 1)

def qc_simpson(f,a,b,n):
    # aceitar se qc = 2^ordem = 16
    tries = []
    for i in range (3):
        tries.append(simpson(f,a,b,n*(2**i)))
    return (tries[1] - tries[0]) / (tries[2] - tries[1])

def error_simpson(f,a,b,n):
    tries = []
    for i in range (3):
        tries.append(simpson(f,a,b,n*(2**i)))
    return (tries[2] - tries[1]) / (2**4 - 1)
