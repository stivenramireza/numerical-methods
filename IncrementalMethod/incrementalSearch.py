import sympy
import math
x = sympy.Symbol('x')
symbols = {'e':math.e,'cos':sympy.cos,'sin':sympy.sin,'ln':sympy.ln}
function  = input("enter the function : ")
function = sympy.sympify(function,locals =symbols)
x0 = input("Value of x : ")

delta = input("value of delta : ")

itera = input("value of iter : ")





def bisec(x0, delta, iter):
    if(delta != 0):
        if(iter > 0 ):
            y0 = function.evalf().subs({x:x0}).evalf()
            if(y0 != 0):
                x1 = x0 + delta
                y1 = function.evalf().subs({x:x1}).evalf()
                cont = 1            
                while ((y1*y0) > 0 and cont < iter):
                    x0 = x1
                    y0 = y1
                    x1 = x0 + delta
                    
                    y1 = function.evalf().subs({x:x1}).evalf()
                    cont = cont + 1
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

bisec(float(x0),float(delta),int(itera))