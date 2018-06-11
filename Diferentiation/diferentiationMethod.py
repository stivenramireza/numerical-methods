import sympy
import math
x = sympy.Symbol('x')
xn =[2,2.1,2.2,2.3,2.4,2.5]
fxn =[-11.8646,-12.4775,-13.0891,-13.6997,-14.3092,-14.9179]
derivs = []
h = xn[1]-xn[0]

function = -0.666666666662422*x**5 + 7.49999999976717*x**4 - 33.7166666650446*x**3 + 75.7649999978021*x**2 - 91.2657666662708*x + 38.6735999999801
#function =  (math.e**-x)-6*x
def eval(valor):
    return (function.evalf().subs({x:valor}))

def dosPuntos(x0, fx0):
    derivs.append((eval(x0+h)-fx0)/h)

def tresPuntos(x0, fx0):
    derivs.append((x0,(eval(x0+h)-eval(x0-h))/(2*h)))

def cincoPuntos(x0, fx0):
    derivs.append((eval(x0-2*h)-8*eval(x0-h)+8*eval(x0+h)-eval(x0+2*h))/(12*h))

    
for i in range(0,len(xn)):
    cincoPuntos(xn[i],fxn[i])
for i in derivs:
    print(i)