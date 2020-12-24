#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:25:45 2020

@author: bdmendes
"""

import math
from real_functions_roots_interval import *
from real_functions_roots_non_interval import *


print(bissection_absolute_precision(lambda x: -x + 4, 0, 5, 0.1))
print(false_position_max_iterations(lambda x: x * math.e ** (x ** 2 - 4), -1, 5, 40))
print(newton_null_at_guess(lambda x: x**4 + 2*x**3 -x -1,lambda x: 4*x**3-6*x**2-1,1,0.01))
print(newton_max_iterations(lambda x: x**4 + 2*x**3 -x -1,lambda x: 4*x**3 - 6*x**2 - 1, 1, 400))
