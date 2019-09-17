import matplotlib.pyplot as plt
import numpy as np
def Bisection(f,a,b,tol,max_iteration):
    iter = 0
    while True:
        c = (a+b)/2
        x = f(c)
        y = f(a)
        if x == 0:
            return(c)
        elif (x * y) <0:
            b = c
        else:
            a = c
        iter = iter + 1
        z = (b-a)/2
        if iter > max_iteration:
            return (c, iter)
        if z < tol:
            return (c, iter)

def f(x):
    return(32*x**6-48*x**4+18*x**2-1)

var,iteract = Bisection(f, 1, 2, (5*(10**-4)), 100)
print(var , iteract)
t = np.arange(1,2,.1)
plt.figure(1)
plt.plot(t,f(t), "visual")
plt.savefig("Figure_1_Lab2.eps")
plt.show()


        #iteration counter |x*-C| <=
        #only matplotlib
