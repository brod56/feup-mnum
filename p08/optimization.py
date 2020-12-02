#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:20:53 2020

@author: up201906166
"""

import math

def uni_optimization(f,B,is_min,x1,x2,epsilon):
    x3 = x1
    x4 = x2
    A = B**2
    
    while (abs(x1-x2) > epsilon):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
 
        if is_min:
           if f(x3) < f(x4):
               x2 = x4
           else:
               x1 = x3
        else:
            if f(x3) > f(x4):
               x2 = x4
            else:
               x1 = x3
               
    if is_min:
        my_min = 9999999
        for i in [x1,x2,x3,x4]:
            if f(i) < my_min:
                my_min = i
        return my_min
    else:
        my_max = -9999999
        for i in [x1,x2,x3,x4]:
            if f(i) > my_max:
                my_max = i
        return my_max
    
   
#OPTIMIZATION ONE DIM    
f = lambda x : (2*(x**2) + 1) - 5* math.cos(10*x);
x1 = -1
x2 = 0
B = (math.sqrt(5) - 1) / 2
epsilon = 0.0001

#print(uni_optimization(f,B,True,x1,x2,epsilon))
#print(uni_optimization(f,B,False,x1,x2,epsilon))
#######################################################

def multi_optimization(f,gradient,h,x,y,epsilon): #min
    while (True):
        old_x = x
        old_y = y
        x = old_x - h*gradient[0](old_x,old_y)
        y = old_y - h*gradient[1](old_x,old_y)
        
        print(x,y)
        
        
        if (abs(y-old_y) <= epsilon or abs(x-old_x) <= epsilon):
            break
        
        if f(x,y) < f(old_x,old_y):
            h *= 2
        else:
            h /= 2
            x, y = old_x,old_y
            
    return (x,y)

#OPTIMIZATION MULTI DIM
f = lambda x,y: y**2 - 2*x*y - 6*y + 2*(x**2) + 12
gradient = [(lambda x,y: -2*y + 4*x) , (lambda x,y: 2*y - 2*x - 6)]
epsilon = 0.01

print(multi_optimization(f,gradient,1,1,1,epsilon))

