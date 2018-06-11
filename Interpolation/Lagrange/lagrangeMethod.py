# p(x) = L0(x)f(x0)+...Ln(x)f(xn)
import sympy

x = sympy.Symbol('x')

xn =[2,2.1,2.2,2.3,2.4,2.5]
fxn =[-11.8646,-12.4775,-13.0891,-13.6997,-14.3092,-14.9179]
functions = []
def lagrange():
    for i in range(0,len(xn)):
        numerator = 1
        denominator = 1
        for j in range(0,len(xn)):
            if( i != j):
                
                numerator = numerator * (x-xn[j])
                denominator = denominator * (xn[i]-xn[j])
        functions.append(numerator/denominator)
        
lagrange()
polinomyal = 0
for i in range(0,len(functions)):
    polinomyal = polinomyal + fxn[i]*functions[i]
print(polinomyal)

d = sympy.simplify(polinomyal)
#f = d.evalf().subs({x:2.5})
#print()
print("simplify",d)