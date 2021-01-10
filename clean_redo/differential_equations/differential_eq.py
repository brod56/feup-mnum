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
        
def rk2_two_var(f, x, y, xf, n): # 2 ordem
    h = (xf - x)/n
    for _ in range(n):
        dy = f(x,y)
        new_x = x + h
        new_y = y + h * f(x + h/2, y + dy*(h/2))
        print(new_x,new_y)
        x = new_x
        y = new_y
        
def rk2_three_var(f1, f2, x, y, z, xf, n): # 2 ordem
    h = (xf-x)/n
    for _ in range(n):
        dy = f1(x,y,z)
        dz = f2(x,y,z)
        new_x = x + h
        new_y = y + h * f1(x + h/2, y + dy*(h/2), z + dz*(h/2))
        new_z = y + h * f2(x + h/2, y + dy*(h/2), z + dz*(h/2))
        print(new_x, new_y, new_z)
        x = new_x
        y = new_y
        z = new_z
        
def rk4_two_var(f, x, y, xf, n): # 4 ordem
    h = (xf-x)/n
    for _ in range(n):
        d1 = h*f(x,y)
        d2 = h*f(x + h/2, y + d1/2)
        d3 = h*f(x + h/2, y + d2/2)
        d4 = h*f(x + h, y + d3)
        new_x = x + h
        new_y = y + d1/6 + d2/3 + d3/3 + d4/6
        print(new_x, new_y)
        x = new_x
        y = new_y
        
def rk4_three_var(f1, f2, x, y, z, xf, n): # 4 ordem
    h = (xf-x)/n
    for _ in range(n):
        d1_f1 = h*f1(x,y)
        d2_f1 = h*f1(x + h/2, y + d1_f1/2)
        d3_f1 = h*f1(x + h/2, y + d2_f1/2)
        d4_f1 = h*f1(x + h, y + d3_f1)
        d1_f2 = h*f2(x,y)
        d2_f2 = h*f2(x + h/2, y + d1_f2/2)
        d3_f2 = h*f2(x + h/2, y + d2_f2/2)
        d4_f2 = h*f2(x + h, y + d3_f2)
        new_x = x + h
        new_y = y + d1_f1/6 + d2_f1/3 + d3_f1/3 + d4_f1/6
        new_z = z + d1_f2/6 + d2_f2/3 + d3_f2/3 + d4_f2/6
        print(new_x, new_y, new_z)
        x = new_x
        y = new_y
        z = new_z
        
