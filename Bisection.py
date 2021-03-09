# Henry Song  |  MA375  |  Spring 2021
# Homework #4: Root-Finding Methods
# File: Bisection.py
# Description: Method for bisection method. Default iteration is set to 1000.
#   - Inputs:(f, interval)
#   --- f: lambda representation of function
#   --- interval: array contanining search interval (i.e. [-2, 0])
#   - Output: approximation of root or None if DNE
#==========================================================================

def bisection(f, interval):
    #separate the interval into corresponding a & b (looks simpler)
    a = interval[0]
    b = interval[1]

    #default iteration is set to 1000
    n = 1000

    #checks if a root exists by checking f(a)*f(b) (MUST be negative)
    if f(a)*f(b) >= 0: return None

    for i in range(1, n+1):
        m = (a + b)/2

        #checks if root is the midpoint
        if f(m) == 0: return m
        #checks if different signs
        elif f(a)*f(m) < 0: b = m
        #checks if same signs
        elif f(a)*f(m) > 0: a = m
        
        #print("[", a, ", ", b , "]")
    return (a + b)/2