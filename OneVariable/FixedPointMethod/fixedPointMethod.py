#!/usr/bin/python3
import sympy
import math
from prettytable import PrettyTable

def fixedPoint(x0, tol, ite):
    if (tol >= 0):
        if (ite > 0):
            tXn.append(x0)
            y0 = functionF.evalf().subs({x:x0}).evalf()
            tfXn.append("%e" % y0)
            if (y0 != 0):
                cont = 0
                error = tol + 1
                errorRela.append("")
                tgXn.append("%e" % x0)
                tIter.append(0)
                xa = x0
                while ((y0 != 0) and (error > tol) and (cont < ite)):
                    tXn.append(xa)
                    xn = functionG.evalf().subs({x:xa}).evalf()
                    tgXn.append("%e" % xn)
                    y0 = functionF.evalf().subs({x:xa}).evalf()
                    tfXn.append("%e" % y0)
                    error = math.fabs(xn - xa)
                    errorRela.append("%e" % (error/xn))
                    xa = xn
                    cont = cont + 1
                    tIter.append(cont)
                if (y0 == 0):
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
    table.add_column("g(Xn)",tgXn)
    table.add_column("Error Absoluto",errorRela)
    print(table)

if __name__ == "__main__":
    x = sympy.Symbol('x')
    symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
    functionF  = input("Enter the function f(x) = ")
    functionF = sympy.sympify(functionF,locals = symbols)
    functionG = input("Enter the function g(x) = ")
    functionG = sympy.sympify(functionG, locals = symbols)
    x0 = float(input("Enter the initial point: "))
    tol = float(input("Enter the tolerance: "))
    ite = int(input("Enter N iteraters: "))
    table = PrettyTable()
    tIter = []
    tXn = []
    tfXn = []
    tgXn = []
    errorRela = []
    fixedPoint(x0, tol, ite)