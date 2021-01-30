# All functions suppose a single local minima exists

def min_gradient(f, gradient, p, h, error):
    if error >= h: raise Exception("Error should be less than step, would stagnate!")
    if len(gradient) != len(p): raise Exception("Must have a derivative per variable!")
    count = 0
    while True:
        count += 1
        ng = p.copy()
        for i in range(len(p)):
            ng[i] -= h*gradient[i](*p)
        if any(abs(ng[i] - p[i]) <= error for i in range(len(p))): break
        if f(*ng) >= f(*p):
            h = h/2
        else:
            h *= 2
            p = ng.copy()
        print(p)

    return p, count

f = lambda x,y: (x+2)**2 + (y+2)**2 - 5
gradient = [lambda x,y: 2*(x+2), lambda x,y: 2*(y+2)]
p = [138467, -2846556]
print(min_gradient(f, gradient, p, 1, 0.01))