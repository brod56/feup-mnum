#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:20:53 2020

@author: up201906166
"""

import math

def multi_optimization_quadric(f,inverse_hessian_v_gradient,x,y,epsilon): #min  
    while (True):
        old_x = x
        old_y = y
        
        mul = np.matmul(inverse_hessian)
        x = old_x - mul[0](old_x,old_y)
        y = old_y - mul[1](old_x,old_y)
        
        print(x,y)
        
        
        if (abs(y-old_y) <= epsilon or abs(x-old_x) <= epsilon):
            break
        
        if f(x,y) < f(old_x,old_y):
            continue
        else:
            print("error! value raised; try new initial point")
            return (-99999999999,-99999999999)
            
    return (x,y)


f = lambda x,y: y**2 - 2*x*y - 6*y + 2*x**2 + 12 + math.cos(4*x)
epsilon = 10**-4
# calculate on maxima
mul =      [   [ (2* (4 - 16* math.cos(4* x))) / (2* (4 - 16* math.cos(4* x)) - 4) , 
                -4 / (2* (4 - 16* math.cos(4* x)) - 4) ] ,
    
                [ -4 / (2* (4 - 16* math.cos(4* x)) - 4) , 
                ((2* (4 - 16* math.cos(4* x))) / (2* (4 - 16* math.cos(4* x)) - 4) ] 
                                                                                           ]


print(multi_optimization_quadric(f,gradient,in_hessian,1,1,epsilon))

