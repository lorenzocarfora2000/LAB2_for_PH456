import numpy as np
from Lab2_main_functions import montecarlo, metropolis, MIS
import matplotlib.pyplot as plt

#point a:  
n = int(5e5)

def a(x):
    return 2*np.exp(-x**2)    
    
def distribution_a(x):
    return np.exp(-abs(x))* (1-np.exp(-10))/2

start_a, end_a = -10, 10
x0, delta = 0, 1 

list_a = metropolis(x0, delta, n, distribution_a, start_a, end_a)

plt.figure(1)
plt.hist(list_a, bins = (100))
plt.title("Distribution of random walk (a)")
plt.xlabel("considered range")
plt.ylabel("bin population")
plt.grid()
plt.show()

#using classic montecarlo:
sol_a = montecarlo(start_a, end_a, n, a) 
print("classic solution for 5.a: I = {} ± {}".format(sol_a[0], sol_a[1]))

sol_mis_a = MIS(start_a, end_a, n, a, distribution_a, x0, delta)
print("solution for 5.a: I = {} ± {}".format(sol_mis_a[0], sol_mis_a[1]))

  
#for point b

n = int(5e5)

def b(x):
    return 1.5*np.sin(x)  
    
def distribution_b(x):
    return 4*x*(np.pi- x)/np.pi**2 *(3/(2*np.pi))


start_b, end_b = 0 , np.pi
x0, delta = 1.5, 1


list_b = metropolis(x0, delta, n, distribution_b, start_b, end_b)

plt.figure(1)
plt.hist(list_b, bins = (100))
plt.title("Distribution of random walk (b)")
plt.xlabel("considered range")
plt.ylabel("bin population")
plt.grid()
plt.show()


#using classic montecarlo:
sol_b = montecarlo(start_b, end_b, n, b) 
print("classic solution for 5.a: I = {} ± {}".format(sol_b[0], sol_b[1]))

sol_mis_b = MIS(start_b, end_b, n, b, distribution_b, x0, delta)
print("solution for 5.b: I = {} ± {}".format(sol_mis_b[0], sol_mis_b[1]))    
    
    
    
    
