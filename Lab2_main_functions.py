import numpy as np

#all the functions used in Lab 2

def montecarlo(start, end, n, function):
    """
    first pass-in element is "start", hence all the numbers at the 
    bottom of the integrals, while "end" is all the numbers at the top
    of the integrals. "n" is the number of iteration and "function" is the 
    function to integrate.
    
    "per_row" is the number of "integrals" and hence the number of variables.
    The append is used for 1D cases, as it puts an integer element into an 
    array.
    """
    
    a  = []
    a = np.append(a, start)
    per_row = len(a)
    
    """
    Each column i of the random_sample is made up of "n" random elements
    chosen between "start_i" and "end_i". The if-else condition
    is applied to ease the writing of 1D integrals, as otherwise "random_vals"
    would be written as a matrix, each element corresponding to a row.
    """
    
    if per_row == 1:
        random_vals = np.random.uniform(start, end, n)
    else:
        random_vals = np.random.uniform(start, end, (n, per_row))
    
    """
    calculation of the average of the function average "f_avg" and the average
    of the squared function "f_squared_avg".
    """
    
    f_avg, f_squared_avg = 0, 0
    
    for x in random_vals:
        value = function(x)
        f_avg += value
        f_squared_avg += value**2
    
    f_avg /= n
    f_squared_avg /= n
    
    """
    The integral solution and its corresponding Root Mean Squared (RMS) are
    calculated and returned as solutions of the function.
    """
    
    interval = end - start
    
    Integral = np.prod(interval)*f_avg
    
    variance = abs(f_squared_avg - f_avg**2)/n
    RMS = np.sqrt(variance)
    return Integral, RMS


def metropolis(x0, delta, n, distribution, start, end):
    
    """
    The accepted values are the starting point of the random walk "x0", the 
    imposed step "delta", the number of computed iterations "n", the 
    probability distribution function "distribution", and the boundaries in 
    which the random walk has to stay, "start" and "end".
    
    a "path" array is set, and it will contain all the iterations of the random
    walk. Since only around less than a half of the iterations will be kept to
    reduce the influence of x0 on the behaviours, "path" is initially set with
    length n/2.
    """
    
    path = np.zeros(int(n/2))
    
    """
    The following for-loop expresses the metropolis walk process. Here "N" is
    the position in "path" assigned to a value; boundary conditions are set to 
    keep the random walk from exceeding the limits set by our integral. This is
    done by modifying the "x_trial" value accordingly by making it "appear on
    the other side" of the considered set. 
    """
    
    N = 0
    x_i = x0
    for i in range(n-1):
        x_trial = x_i + np.random.uniform(-delta, delta)
        
        if x_trial > end:  x_trial -= (end-start)
        if x_trial < start: x_trial += (end-start)
        
        
        w = distribution(x_trial)/distribution(x_i)
        r = np.random.uniform(0, 1)
        if w >= 1 or (w<1 and w >=r):
            x_i = x_trial
        
        """
        although the "x_i" variable will be modified at each step, it will only
        be attached in the "path" array if the following conditions are met, 
        meaning it has to be n/20 steps away from "x0" and it has to be an even 
        number iteration (hence reducing the number of considered values and 
        their "influence" on each other.
        """
        
        if (i> int(n/20) and i%2 == 0):
            path[N] = x_i
            N += 1
    
    """
    the "empty" positions in "path" are taken out, and the result is returned
    as our set of random values following the imposed "distribution" function. 
    """
    
    return path[:N]


#modified montecarlo, with importance sampling
#the distribution must be normalised
def MIS(start, end, n, function, distribution, x0, delta):
    
    """
    The Montecarlo routine with Importance Sampling (MIS) for 1D problems. The 
    "start", "end", "n" and "function" variables are the same as those in the 
    montecarlo function, and the "distribution", "x0" and "delta" ones are
    the same as those in the metropolis function. It is important to notice 
    that, for the routine to work properly, the "distribution" function must be
    normalised for the considered interval [start, end].
    
    The "random_vals" array is now selected by following the imposed 
    distribution function using the Metropolis algorithm. "N" is defined as 
    being the Number of considered iterations, and hence of the values used to 
    calculate the integral.
    """
    
    random_vals = metropolis(x0, delta, n, distribution, start, end)
    N = len(random_vals)
    
    """
    Similar process as used in the Montecarlo function, only this time we are 
    considering function(x)/distribution(x), which is used to make the process
    diverge faster to the solution. As like the montecarlo function, the 
    solution of the Integral and its corresponding RMS are returned as 
    solutions of the function.
    """
    
    f_avg, f_squared_avg = 0, 0
    
    for x in random_vals:
        value = function(x)/distribution(x)
        f_avg += value
        f_squared_avg += value**2
    
    f_avg /= N
    f_squared_avg /= N
    
    Integral = f_avg
    
    variance = abs(f_squared_avg - f_avg**2)/N
    RMS = np.sqrt(variance)
    
    return Integral , RMS
 



















