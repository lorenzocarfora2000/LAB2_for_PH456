import numpy as np
from math import gamma
from Lab2_main_functions import montecarlo

###Task 3 ###

#The following problem will assume the considered radius r = 2.

#analytical function for the volume of a n-sphere
def hypervolume(r, D):
   return ((np.sqrt(np.pi)*r)**D)/gamma(1 + D/2)

#Step-function
def step_function(coords):
    r = np.sqrt(sum(coords**2))
    return int(r <= 2.0)        #returns 1 if true, 0 if false

#imposed number of considered iterations
n = int(3e6)

#boundaries for a 3-sphere volume (the volume of a ball), radius = 2:
start, end = -2*np.ones(3), 2*np.ones(3)

vol_3sphere = hypervolume(2, 3)
int_3sphere = montecarlo(start, end, n, step_function)

print("the volume of a 3-sphere is: {} ".format(vol_3sphere))
print("montecarlo found it to be: {} ± {}".format(int_3sphere[0], int_3sphere[1]))

#Boundaries for a 5-sphere volume, radius = 2:
start, end = -2*np.ones(5), 2*np.ones(5)

vol_5sphere = hypervolume(2, 5)
int_5sphere = montecarlo(start, end, n, step_function)

print("the volume of a 5-sphere is: {} ".format(vol_5sphere))
print("montecarlo found it to be: {} ± {}".format(int_5sphere[0], int_5sphere[1]))

#Task 4

#function defining the Integrand of the problem
def function(coords):
    a, b, c = coords[:3], coords[3:6], coords[6:]
    term  = np.abs(np.dot(a+b, c))
    return 1/term

start = np.zeros(9)
end = np.ones(9)
n = int(1e6)

I = montecarlo(start, end, n, function)
percentage = I[1]/I[0]*100

print("the result of Task 4 is I = {} ± {}".format(I[0], I[1]))
print("  and it has precision: {} %".format(percentage))


