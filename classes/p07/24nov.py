#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:47:03 2020

@author: up201906166
"""

#MALFUNCTIONING...

def euler(f,g,a,b,h,x0,y0,z0):
    # xn é o x em cada passo
    x = x0
    y = y0
    z = z0
    
    while x < b-h/2: # allow error
        y += h * f(x, y, z)
        z += h * g(x, y, z)
        x += h
        
    return (x,y,z)

def qc_euler_y(f,g,a,b,n,x0,y0,z0):
    S = []
    for i in range(3):
        S.append(euler (f,g,a,b,h / (2**i),x0,y0,z0) )
    return (S[1][0]-S[0][0])/(S[2][0]-S[1][0])

def qc_euler_z(f,g,a,b,h,x0,y0,z0):
    S = []
    for i in range(3):
        S.append(euler (f,g,a,b,h / (2**i),x0,y0,z0) )
    return (S[1][1]-S[0][1])/(S[2][1]-S[1][1])

f = lambda x,y,z : z*y + x
g = lambda x,y,z : z*x + y
h = 0.1

print(euler(f,g,0,0.5,h,0,1,1))
print(qc_euler_y(f,g,0,0.5,h,0,1,1))
print(qc_euler_z(f,g,0,0.5,h,0,1,1))