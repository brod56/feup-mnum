import math

def trapezoidal(f, a, b, n):
    h = (a+b)/n
    return h/2 * (f(a) + f(b) + 2*sum(f(a+i*h) for i in range(1, n)))

def simpson(f, a, b, n):
    h = (a+b)/n
    return h/3 * (f(a) + f(b) + sum(4*f(a+i*h) if i%2 != 0 else 2*f(a+i*h) for i in range(1,n)))

def qc(method, f, a, b, n):
    tries = [method(f,a,b,n*(2**i)) for i in range(3)]
    return (tries[1] - tries[0]) / (tries[2]-tries[1])

def error(method, order, f, a, b, n, tolerance_qc):
    if abs(qc(method, f, a, b, n)-2**order) > tolerance_qc: return False
    tries = [method(f,a,b,n*(2**i)) for i in range(3)]
    return (tries[2]-tries[1])/(2**order - 1)


if __name__ == '__main__':
    import math
    f = lambda x:(x**2 * math.sin(x))/5
    a,b = 0, 20*math.pi + 0.5
    for n in [2,4,8,16,100,200,400,800,1000000]:
        for func in [simpson, trapezoidal]:
            print("Simpson: " if func == simpson else "Trapezoidal: ",
                  func(f,a,b,n), qc(func, f,a,b,n),
                    error(func, 2 if func==trapezoidal else 4, f,a,b,n,0.2))
        print()
