import matplotlib.pyplot as mp
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
            print("iteration limit")
            return (c, iter)
        if z < tol:
            print("tolerance limit")
            return (c, iter)

def f(x):
    return(x**6-x-1)
print (f)
var,iteract = Bisection(f, 1, 2, (5*(10**-4)), 100)
print(var , iteract)




        #iteration counter |x*-C| <=
        #only matplotlib
