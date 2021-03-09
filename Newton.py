# Henry Song  |  MA375  |  Spring 2021
# Homework #4: Root-Finding Methods
# File: Newton.py
# Description: Method for Newton's method. Default iteration is set to 1000.
#   - Inputs:(f, interval)
#   --- f: lambda representation of function
#   --- interval: array contanining search interval (i.e. [-2, 0])
#   - Output: approximation of root or None if DNE
#==========================================================================

def newton(f, f_prime, x0, epsilon):
    max_iter = 1000
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        f_primexn = f_prime(xn)
        if f_primexn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/f_primexn
    print('Exceeded maximum iterations. No solution found.')
    return None