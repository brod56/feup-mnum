def euler(f, x, y, h, n):
    l = [(x,y)]
    for _ in range(n):
        nx = x + h
        ny = y + h*f(x,y)
        l.append((nx,ny))
        x = nx
        y = ny
    return l


def rk2(f, x, y, h, n):
    l = [(x,y)]
    for _ in range(n):
        nx = x + h
        ny = y + h*f(x + h/2,y + h/2*f(x,y))
        l.append((nx,ny))
        x = nx
        y = ny
    return l


def rk4(f, x, y, h, n):
    l = [(x,y)]
    for _ in range(n):
        d1 = h*f(x,y)
        d2 = h*f(x + h/2, y + d1/2)
        d3 = h*f(x + h/2, y + d2/2)
        d4 = h*f(x + h, y + d3)
        nx = x + h
        ny = y + d1/6 + d2/3 + d3/3 + d4/6
        l.append((nx,ny))
        x = nx
        y = ny
    return l


if __name__ == '__main__':
    dy = lambda x,y: x - 2
    print(euler(dy, 0, 3, 0.25, 5))
    print(rk2(dy, 0, 3, 0.25, 5))
    print(rk4(dy, 0, 3, 0.25, 5))