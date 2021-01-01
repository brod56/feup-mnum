def euler_two_var(f, x, y, xf, n): #1 ordem
    h = (xf-x)/n
    for _ in range(n):
        new_x = x + h
        new_y = h*f(x,y)
        print(new_x,new_y)
        x = new_x
        y = new_y
        
def euler_three_var(f1, f2, x, y, z, xf, n): # 1 ordem
    h = (xf-x)/n
    for _ in range(n):
        new_x = x + h
        new_y = y + h*f1(x,y,z)
        new_z = z + h*f2(x,y,z)
        print(new_x,new_y,new_z)
        x = new_x
        y = new_y
        z = new_z
        
def rk2_two_var(f, x, y, z, xf, n): # 2 ordem
    h = (xf - x)/n
    for _ in range(n):
        dy = h*f(x,y,z)
        new_x = x + h
        new_y = y + h * f(x + h/2, y + dy*(h/2))
        print(new_x,new_y)
        x = new_x
        y = new_y
        
def rk2_three_var(f1, f2, x, y, z, xf, n): # 2 ordem
    h = (xf-x)/n
    for _ in range(n):
        dy = h*f1(x,y,z)
        dz = h*f2(x,y,z)
        new_x = x + h
        new_y = y + h * f1(x + h/2, y + dy*(h/2), z + dz*(h/2))
        new_z = y + h * f2(x + h/2, y + dy*(h/2), z + dz*(h/2))
        print(new_x, new_y)
        x = new_x
        y = new_y
        z = new_z
        
