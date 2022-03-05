import numpy as np
from Lab2_main_functions import montecarlo

#Task 2:
    
n = int(1e6)

def a(coord):
    return 2

start_a, end_a = 0, 1

sol_a = montecarlo(start_a, end_a, n, a) 
print("solution for 2.a: I = {} ± {}".format(sol_a[0], sol_a[1]))

def b(x):
    return -x

start_b, end_b = 0, 1

sol_b = montecarlo(start_b, end_b, n, b) 
print("solution for 2.b: I = {} ± {}".format(sol_b[0], sol_b[1]))


def c(x):
    return x**2

start_c, end_c = -2, 2

sol_c = montecarlo(start_c, end_c, n, c) 
print("solution for 2.c: I = {} ± {}".format(sol_c[0], sol_c[1]))


def d(coord):
    x, y = coord
    return x*y + x

start_d, end_d = np.array([0, 0]), np.array([1, 1])

sol_d = montecarlo(start_d, end_d, n, d) 
print("solution for 2.d: I = {} ± {}".format(sol_d[0], sol_d[1]))


