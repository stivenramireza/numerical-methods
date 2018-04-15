#!/usr/bin/python3
import sympy
import math
from prettytable import PrettyTable

def bisec(xi, xs, tol, ite):
    errorRela.append("")
    tXi.append(xi)
    tXs.append(xs)
    if (tol >= 0):
        if (ite > 0):
            yi = function.evalf().subs({x:xi}).evalf()
            if (yi != 0):
                ys = function.evalf().subs({x:xs}).evalf()
                if (ys != 0):
                    if (yi*ys < 0):
                        xm = (xi + xs) / 2
                        tXm.append(xm)
                        ym = function.evalf().subs({x:xm}).evalf()
                        tfXm.append("%e" %(ym))
                        error = tol + 1
                        cont = 1
                        tIter.append(cont)

                        while((ym != 0) and (error > tol) and (cont < ite)):
                            if yi*ym < 0:
                                xs = xm
                                ys = ym
                            else:
                                xi = xm
                                yi = ym
                            tXs.append(xs)
                            tXi.append(xi)
                            xaux = xm
                            xm = (xi + xs) / 2
                            tXm.append(xm)
                            ym = function.evalf().subs({x:xm}).evalf()
                            tfXm.append("%e" % (ym))
                            error = math.fabs(xm - xaux)
                            errorRela.append("%e" % (error/xm))
                            cont = cont + 1
                            tIter.append(cont)
                        
                        if(ym == 0):
                            print (str(xm) + " is an aproximate root")
                        elif(error < tol):
                            print (str(xaux) + " is an aproximate root")
                        else:
                            print ("Failed!")
                    else:
                        print ("Failed the interval!")
                else:
                    print (str(xs) + "is a root")
            else:
                print (str(xi) + " is a root")
        else:
            print ("Wrong iterates!")
    else:
        print ("Tolerance < 0")
    table.add_column("n",tIter)
    table.add_column("Xi",tXi)
    table.add_column("Xs",tXs)
    table.add_column("Xm",tXm)
    table.add_column("f(Xm)",tfXm)
    table.add_column("Error Relativo",errorRela)
    print(table)
                      
if __name__ == "__main__":
    x = sympy.Symbol('x')
    symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
    function  = input("Enter the function : ")
    function = sympy.sympify(function,locals =symbols)
    xi = float(input("Enter the first point: "))
    xs = float(input("Enter the last point: "))
    tol = float(input("Enter the tolerance: "))
    ite = int(input("Enter N iteraters: "))
    table = PrettyTable()
    tIter = []
    tXi = []
    tXs = []
    tXm = []
    tfXm = []
    errorRela = []
    bisec(xi, xs, tol, ite)