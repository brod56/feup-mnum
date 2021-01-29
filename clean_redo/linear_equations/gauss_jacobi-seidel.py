#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gauss_jacobi(m, b, max_iter, g, seidel):
    if len(m) != len(b) or len(m) != len(m[0]) or len(g) != len(m):
        return False

    #check dominant diagonal
    for i in range(len(m)):
        if m[i][i] <= sum(m[i][j] if j != i else 0 for j in range(len(m[0]))):
            return False

    sols = [0 for _ in range(len(m))]
    for i in range(max_iter):
        for l in range(len(m)):
            sols[l] = (1/m[l][l]) * (b[l] - sum(g[j]*m[l][j] if j!= l else 0 for j in range(len(m[0]))))
            if seidel: g[l] = sols[l]
        g = sols.copy()
        print(g)

    return sols