import sympy
from prettytable import PrettyTable
import totalPivotingMethod
x = sympy.Symbol('x')
table = PrettyTable()

xn =[1,3,4,5,7]
fxn =[4.31,1.5,3.2,2.6,1.8]

inequality =[]
functions =[]
result =[]
des = []
'''
y-y1 = m(x-x1)

y = y1+((y1-y0)/(x1-x0))*(x-x1)
'''

def createInequality():
    for i in range(0,len(xn)-1):
        if(i < len(xn)):
            inequality.append(((xn[i],fxn[i]),(xn[i+1],fxn[i+1])))

def linear():
    
    for i in inequality:
        print(i)
        y = i[1][1]+((i[1][1]-i[0][1])/(i[1][0]-i[0][0])*(x-i[1][0]))
        result.append(y)
        des.append(str(i[0][0]) + " <= x <= " +str(i[1][0]))
    table.add_column("equations",result)
    table.add_column("inequality",des)
    print(table)

    
createInequality() 

linear()


