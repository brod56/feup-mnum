#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gauss_jacobi(m, res, x1, x2, x3, error): # must be 3x3
    n_x1 = x1
    n_x2 = x2
    n_x3 = x3
    x1_ger = lambda x2,x3: (res[0][0] - m[0][1]*x2 - m[0][2]*x3)/m[0][0]
    x2_ger = lambda x1,x3: (res[1][0] - m[1][0]*x1 - m[1][2]*x3)/m[1][1]
    x3_ger = lambda x1,x2: (res[2][0] - m[2][0]*x1 - m[2][1]*x2)/m[2][2]
    while (True):
        n_x1 = x1_ger(x2,x3)
        n_x2 = x2_ger(x1,x3)
        n_x3 = x3_ger(x1,x2)
        if (abs(n_x1 - x1) <= error or abs(n_x2 - x2) <= error or abs(n_x3 - x3) <= error):
            break
        x1 = n_x1
        x2 = n_x2
        x3 = n_x3
        
    return n_x1, n_x2, n_x3

def gauss_seidel(m, res, x1, x2, x3, error): # must be 3x3
    n_x1 = x1
    n_x2 = x2
    n_x3 = x3
    x1_ger = lambda x2,x3: (res[0][0] - m[0][1]*x2 - m[0][2]*x3)/m[0][0]
    x2_ger = lambda x1,x3: (res[1][0] - m[1][0]*x1 - m[1][2]*x3)/m[1][1]
    x3_ger = lambda x1,x2: (res[2][0] - m[2][0]*x1 - m[2][1]*x2)/m[2][2]
    while (True):
        n_x1 = x1_ger(x2,x3)
        n_x2 = x2_ger(n_x1,n_x3)
        n_x3 = x3_ger(n_x1,n_x2)
        if (abs(n_x1 - x1) <= error or abs(n_x2 - x2) <= error or abs(n_x3 - x3) <= error):
            break
        x1 = n_x1
        x2 = n_x2
        x3 = n_x3
        
    return n_x1, n_x2, n_x3
