# Henry Song  |  MA375  |  Spring 2021
# Homework #4: Root-Finding Methods
# File: Driver.py
# Description: Driver class for each individual root-finding method
#   - Inputs:(x)
#   --- x: value of x
#   - Output: value of function
#==========================================================================

from Bisection import bisection
from Newton import newton
from Secant import secant
from Falsi import falsi
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib

def plot(func):
    x = np.arange(-4, 4, 0.1) #Creates x values from -4 to 4 with an interval of 0.1
    y = np.asarray(list(map(func, x))) #uses f(x) to create array of y-values

    # axis adjustments
    axes = plt.axes()
    axes.set_ylim([-10, 10])
    plt.axhline(y=0, color='red')
    plt.axvline(x=0, color='red')

    #plots function
    plt.plot(x, y, 'b-')
    plt.grid(True)
    plt.show()


# Function definitions
x = sym.symbols('x')
equation = 5*(x**3) - 20*(x**2) + 5*x + 30  # equation that will be used for root-finding methods
f = sym.lambdify(x, equation)   #lambda representation of equation
f_prime = sym.lambdify(x, sym.diff(equation))   #lambda representation of derivative of equation

#interval definitions
interval_1 = [-2, 0]
interval_2 = [0, 2.5]
interval_3 = [2.5, 4]

print()
print("Root Finding Driver Class")
print("By Henry Song")
print()
print("Using f(x) = ", equation, " over ", interval_1, ", ", interval_2, ", ", interval_3)
print()

#continuous loop to run each method individually with user selecting used method each iteration
while(True):
    print("Enter 1 for Bisection Method")
    print("Enter 2 for Newton's Method")
    print("Enter 3 for Secant Method")
    print("Enter 4 for False Method")
    print("Enter any other number to quit")
    option = int(input("Select option: "))

    print()

    if option == 1:
        print("Bisection Method:")
        print("Over interval [-2, 0]:\t", bisection(f, interval_1))
        print("Over interval [0, 2.5]:\t", bisection(f, interval_2))
        print("Over interval [2.5, 4]:\t", bisection(f, interval_3))
    elif option == 2:
        print("Newton's Method:")
        print("Over interval [-2, 0]:\t", newton(f, f_prime, -2, 0.000000001))
        print("Over interval [0, 2.5]:\t", newton(f, f_prime, 1, 0.000000001))
        print("Over interval [2.5, 4]:\t", newton(f, f_prime, 4, 0.000000001))
    elif option == 3:
        print("Secant Method:")
        print("Over interval [-2, 0]:\t", secant(f, interval_1))
        print("Over interval [0, 2.5]:\t", secant(f, interval_2))
        print("Over interval [2.5, 4]:\t", secant(f, interval_3))
    elif option == 4:
        print("Falsi Method:")
        print("Over interval [-2, 0]:\t", falsi(f, interval_1))
        print("Over interval [0, 2.5]:\t", falsi(f, interval_2))
        print("Over interval [2.5, 4]:\t", falsi(f, interval_3))
    else:
        break

    plot(f)
    print("----------------------------------------------------")
    print()
    