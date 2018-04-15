#!/usr/bin/python3
import sympy
import math
from prettytable import PrettyTable
x = sympy.Symbol('x')

f = (math.e**(((-x)**2)+5)) + sympy.ln(x**2 + 3) - 4*x + 45
g = x-f/f.diff(x)
tol = 0.00001
xa = 0
table = PrettyTable()

iters = []
funcG = []
funcF = []
errorTot = []
deriv = []

def newton(tol,xa,niter):
    fx = f.evalf().subs({x:xa})
    funcF.append("%e" % (fx))
    error = tol+1
    errorTot.append("")
    funcG.append((xa))
    deriv.append(f.diff(x).evalf().subs({x:xa}))
    iters.append(0)
    cont = 0
    while(fx != 0 and error > tol and cont < niter):        
        xn = g.evalf().subs({x:xa}).evalf()        
        funcG.append((xn))
        deriv.append(f.diff(x).evalf().subs({x:xn}).evalf())
        fx = f.evalf().subs({x:xn}).evalf()
        funcF.append("%e" % (fx))
        error = abs(xn-xa)
        errorTot.append("%e" % (error/xn))
        xa = xn
        cont = cont +1
        iters.append(cont)
    if ( fx == 0):
        print(str(xa)+" es raiz")
    elif (error < tol):
        print(str(xa)+" es una aproximacion ")
    else: 
        print("El metodo fracasó")
    table.add_column("n",iters)
    table.add_column("xn",funcG)
    table.add_column("f(xn)",funcF)
    table.add_column("f'(xn)",deriv)
    table.add_column("error",errorTot)
    print(table)
    
newton(tol,xa,200)