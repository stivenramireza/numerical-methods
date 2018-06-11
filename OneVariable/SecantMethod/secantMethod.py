import sympy
import math
from prettytable import PrettyTable
x = sympy.Symbol('x')
table = PrettyTable()

iters = []
xn = []
funcF = []
funcD1 = []
funcD2 = []
errorTot = []

def secant(tol,x0,niter):
    if(tol >= 0):
        if (ite > 0):    
            fx0 = f.evalf().subs({x:x0})
            if(fx0 != 0):
                fx1 = f.evalf().subs({x:x0}).evalf()
                funcF.append(fx1)
                error = tol+1
                errorTot.append(0)
                iters.append(0)
                xn.append(x0)
                cont = 0
                aux0 = x0
                while(fx1 != 0 and den != 0 and error > tol and cont < niter):        
                    xn.append(aux1)
                    aux2 = aux1-f.evalf().subs({x:aux1}).evalf()*(aux1-aux0)/den
                    error = abs(aux2-aux1)
                    errorTot.append(error)
                    aux0 = aux1
                    fx0 = fx1
                    aux1 = aux2
                    fx1 = f.evalf().subs({x:aux1}).evalf()
                    funcF.append(fx1)
                    cont = cont + 1
                    iters.append(cont)
                if ( fx1 == 0):
                    print(str(aux1)+" Is a root")
                elif (error < tol):
                    print(str(aux1)+" Is an aproximate root")
                else: 
                    print("The method failed")
                table.add_column("n",iters)
                table.add_column("xn",xn)
                table.add_column("f(xn)",funcF)
                table.add_column("error",errorTot)
                print(table)
            else:
                print("x0 Is a root",x0)
        else:
            print("Wrong iterates")
    else:
        print("Tolerance < 0")


if __name__ == "__main__":
    x = sympy.Symbol('x')
    symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
    function  = input("Enter the function f(x) = ")
    function = sympy.sympify(function,locals = symbols)
    f = function
    fd1 = sympy.diff(f)
    fd2 = sympy.diff(fd1)
    x0 = float(input("Enter the x0 point: "))
    tol = float(input("Enter the tolerance: "))
    ite = int(input("Enter N iteraters: "))
    secant(tol,x0,ite)