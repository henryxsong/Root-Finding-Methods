# Henry Song  |  MA375  |  Spring 2021
# Homework #4: Root-Finding Methods
# File: Falsi.py
# Description: Method for Regular Falsi method. Default iteration is set to 1000.
#   - Inputs:(f, interval)
#   --- f: lambda representation of function
#   --- interval: array contanining search interval (i.e. [-2, 0])
#   - Output: approximation of root or None if DNE
#==========================================================================

def falsi(f, interval):
    #separate the interval into corresponding a & b (looks simpler)
    a = interval[0]
    b = interval[1]

    #default iteration is set to 1000
    n = 1000

    #checks if a root exists by checking f(a)*f(b) (MUST be negative)
    if f(a) * f(b) >= 0: return None
      
    for i in range(n): 
        # Find the point that touches x axis 
        x2 = b - f(b)*((b-a)/(f(b)-f(a)))

        # checks if root is found
        if f(x2) == 0: break
        # shifts variables
        elif f(a) * f(x2) < 0: b = x2 
        elif f(a)*f(x2) > 0: a = x2 
        else: return None   #does not converge
    return b - f(b)*((b-a)/(f(b)-f(a)))