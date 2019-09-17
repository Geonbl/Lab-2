#ultimatly we want ot find the aproximatino of root zero.
import numpy as np
import sympy as sp
x = sp.symbols("x")
def Newton(f,fp,xn,tol):
    iter = 0
    while True:
        a = (f(xn))/(fp(xn))
        xn = xn - a
        z=f(xn)
        iter += 1
        zt = abs(z)
        if zt < tol:
            print (iter)
            return(f(z))
        if iter > 100:
            print (iter)
            return(f(z))


def f(x):
    x**6-x-1.0
fp = sp.diff(f)
var = Newton (f,fp,1.0,10*-10)
print(var)
