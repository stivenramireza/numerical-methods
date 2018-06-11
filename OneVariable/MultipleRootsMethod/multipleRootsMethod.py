#!/usr/bin/python3
import sympy
import math
from prettytable import PrettyTable

def multipleRoots(x0, tol, ite):
    if (tol >= 0):
        if (ite > 0):
            tXn.append(x0)
            y0 = functionF.evalf().subs({x:x0}).evalf()
            tfXn.append("%e" % y0)
            y0p1 = functionFP1.evalf().subs({x:x0}).evalf()
            tfp1Xn.append("%e" % y0p1)
            y0p2 = functionFP2.evalf().subs({x:x0}).evalf()
            tfp2Xn.append("%e" % y0p2)
            if (y0 != 0):
                cont = 0
                error = tol + 1
                errorAbsoluto.append("")
                tIter.append(0)
                xa = x0
                while ((y0 != 0) and (y0p1 != 0) and (y0p2 != 0) and (error > tol) and (cont < ite)):
                    xn = xa - ((y0*y0p1) / ((y0p1**2) - (y0*y0p2)))
                    tXn.append(xn)
                    y0 = functionF.evalf().subs({x:xn}).evalf()
                    tfXn.append("%e" % y0)
                    y0p1 = functionFP1.evalf().subs({x:xn}).evalf()
                    tfp1Xn.append("%e" % y0p1)
                    y0p2 = functionFP2.evalf().subs({x:xn}).evalf()
                    tfp2Xn.append("%e" % y0p2)
                    error = math.fabs(xn - xa)
                    errorAbsoluto.append("%e" % error)
                    xa = xn
                    cont = cont + 1
                    tIter.append(cont)
                if (y0 == 0):
                    print (str(xa) + " is a root")
                elif (y0p1 == 0):
                    print (str(xa) + " is a root")
                elif (y0p2 == 0):
                    print (str(xa) + " is a root")
                elif (error <= tol):
                    print (str(xa) + " is an aproximate root")
                else:
                    print ("Failed the interval!")
            else:
                print (str(x0) + " is a root")
        else:
            print ("Wrong iterates!")
    else:
        print ("Tolerance < 0")
    table.add_column("n",tIter)
    table.add_column("Xn",tXn)
    table.add_column("f(Xn)",tfXn)
    table.add_column("f'(Xn)",tfp1Xn)
    table.add_column("f''(Xn)",tfp2Xn)
    table.add_column("Error",errorAbsoluto)
    print(table)

if __name__ == "__main__":
    x = sympy.Symbol('x')
    symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
    functionF  = input("Enter the function f(x) = ")
    functionF = sympy.sympify(functionF,locals = symbols)
    functionFP1 = sympy.diff(functionF)
    functionFP2 = sympy.diff(functionFP1)
    x0 = float(input("Enter the initial point: "))
    tol = float(input("Enter the tolerance: "))
    ite = int(input("Enter N iteraters: "))
    table = PrettyTable()
    tIter = []
    tXn = []
    tfXn = []
    tfp1Xn = []
    tfp2Xn = []
    errorAbsoluto = []
    multipleRoots(x0, tol, ite)