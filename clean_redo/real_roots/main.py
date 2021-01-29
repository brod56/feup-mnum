from real_functions_roots_interval import *
from real_functions_roots_non_interval import *

g = lambda x: (6/x +5)/3
guess = 3

print(picard_peano_max_iterations(g, guess, 5))