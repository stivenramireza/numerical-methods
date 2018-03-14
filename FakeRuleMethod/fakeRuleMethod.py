#!/usr/bin/python3
import sympy
import math

def fakeRule(xi, xs, tol, ite):
    if (tol >= 0):
        if (ite > 0):
            yi = function.evalf().subs({x:xi}).evalf()
            if (yi != 0):
                ys = function.evalf().subs({x:xs}).evalf()
                if (ys != 0):
                    if (yi*ys < 0):
                        xm = xi - ((yi*(xi-xs))/(yi-ys))
                        ym = function.evalf().subs({x:xm}).evalf()
                        error = tol + 1
                        cont = 1

                        while((ym != 0) and (error > tol) and (cont < ite)):
                            if yi*ym < 0:
                                xs = xm
                                ys = ym
                            else:
                                xi = xm
                                yi = ym
                            
                            xaux = xm
                            xm = xi - ((yi*(xi-xs))/(yi-ys))
                            ym = function.evalf().subs({x:xm}).evalf()
                            error = math.fabs(xm - xaux)
                            cont = cont + 1
                        
                        if(ym == 0):
                            print (str(xm) + " is a aproximate root")
                        elif(error < tol):
                            print (str(xaux) + " is a aproximate root")
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
                      
if __name__ == "__main__":
    x = sympy.Symbol('x')
    symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
    function  = input("Enter the function : ")
    function = sympy.sympify(function,locals =symbols)
    xi = float(input("Enter the first point: "))
    xs = float(input("Enter the last point: "))
    tol = float(input("Enter the tolerance: "))
    ite = int(input("Enter N iteraters: "))
    fakeRule(xi, xs, tol, ite)