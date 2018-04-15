import sympy
import math
from prettytable import PrettyTable

x = sympy.Symbol('x')
symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
function  = input("enter the function : ")
function = sympy.sympify(function,locals =symbols)
x0 = input("Value of x : ")

delta = input("value of delta : ")

itera = input("value of iter : ")

table = PrettyTable()
iters = []
funcF = []
vXn = []

def bisec(x0, delta, iter):
    vXn.append(x0)
    iters.append(0)
    if(delta != 0):
        if(iter > 0 ):
            y0 = function.evalf().subs({x:x0}).evalf()
            funcF.append(y0)
            if(y0 != 0):
                x1 = x0 + delta
                vXn.append(x1)
                y1 = function.evalf().subs({x:x1}).evalf()
                funcF.append(y1)
                cont = 1
                iters.append(cont)            
                while ((y1*y0) > 0 and cont < iter):
                    x0 = x1
                    y0 = y1
                    x1 = x0 + delta
                    vXn.append(x1)
                    y1 = function.evalf().subs({x:x1}).evalf()       
                    funcF.append(y1)
                    cont = cont + 1
                    iters.append(cont)
                if(y1 == 0):
                    print(str(x1) + " is a root")
                elif( y1*y0 < 0):
                    print(str((x0,x1))+" is an interval")
                else:
                    print("Failed!")
            else:
                print(str(x0)+" is a root")    
        else:
            print("Wrong iterates!")
    else:
        print("Delta zero")
    table.add_column("n",iters)
    table.add_column("Xn",vXn)
    table.add_column("f(Xn)",funcF)
    print(table)

bisec(float(x0),float(delta),int(itera))