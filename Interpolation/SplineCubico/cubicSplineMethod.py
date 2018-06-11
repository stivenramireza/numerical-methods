import sympy
from prettytable import PrettyTable
import totalPivoting
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
    
createInequality() 

def cubic():
    superMatrix = [[0 for x in range(4*len(inequality)+1)] for y in range(4*len(inequality))] 
    n = len(superMatrix)
    j = 0
    z = 0
    l = 0
    #normal
    result.append("anx**3 + bnx**2 +cnx+dn")
    des.append("normal")
    for i in inequality:
        auxj = str(z-j-l)
        equation = str(i[0][0]**3)+"a"+auxj+" + "+str(i[0][0]**2)+"b"+auxj+" + "+str(i[0][0])+"c"+auxj+" + d"+auxj+" = " + str(i[0][1])
        superMatrix[j][z] = i[0][0]**3
        superMatrix[j][z+1] = i[0][0]**2
        superMatrix[j][z+2] = i[0][0]
        superMatrix[j][z+3] = 1
        superMatrix[j][n] = i[0][1]
        result.append(equation)
        des.append("x = "+str(i[0][0]) )
        
        equation = str(i[1][0]**3)+"a"+auxj+" + "+str(i[1][0]**2)+"b"+auxj+" + "+str(i[1][0])+"c"+auxj+" + d"+auxj+" = " + str(i[1][1])
        superMatrix[j+1][z] = i[1][0]**3
        superMatrix[j+1][z+1] = i[1][0]**2
        superMatrix[j+1][z+2] = i[1][0]
        superMatrix[j+1][z+3] = 1
        superMatrix[j+1][n] = i[1][1]
        result.append(equation)
        des.append("x = " +str(i[1][0]))
        z += 4
        j += 2
        l += 1
    k = j
    z = 0
    result.append("  ")
    des.append("  ")
    result.append("3anx**2 + 2xbn + cn = 3an+1x**2 + 2xbn+1 + cn+1")
    des.append("first derivative")
    for i in range(0,len(inequality)-1):
        superMatrix[k][z] = 3*inequality[i][1][0]**2
        superMatrix[k][z+1] = 2*inequality[i][1][0]
        superMatrix[k][z+2] = 1
        superMatrix[k][z+4] = -3*inequality[i+1][0][0]**2
        superMatrix[k][z+5] = -2*inequality[i+1][0][0]
        superMatrix[k][z+6] = -1
        superMatrix[k][n] = 0
        equation = str(3*inequality[i][1][0]**2)+"a"+str(i) + " + "+str(2*inequality[i][1][0])+ "b"+str(i) + " + c"+str(i)+" = " + str(3*inequality[i+1][0][0]**2)+"a"+str(i+1) + " + "+str(2*inequality[i+1][0][0])+ "b"+str(i+1) + " + c"+str(i+1)
        result.append(equation)
        desig = "with  x <= "+str(inequality[i][1][0])+" & "+ str(inequality[i+1][0][0]) +" <= x"
        des.append(desig)
        k += 1
        z += 4
    
    
    z = 0
    result.append("  ")
    des.append("  ")
    result.append("6anx + 2bn = 6anx + 2bn")
    des.append("second derivative")   
    for i in range(0,len(inequality)-1):
        superMatrix[k][z] = 6*inequality[i][1][0]
        superMatrix[k][z+1] = 1
        superMatrix[k][z+3] = -6*inequality[i+1][0][0]**2
        superMatrix[k][z+4] = -1
        superMatrix[k][n] = 0
        equation = str(6*inequality[i][1][0])+"a"+str(i) + " + 2b"+str(i)+" = " + str(6*inequality[i+1][0][0])+"a"+str(i+1) + " + 2b"+str(i+1) 
        result.append(equation)
        desig = "with  x <= "+str(inequality[i][1][0])+" & "+ str(inequality[i+1][0][0]) +" <= x"
        des.append(desig)
        k += 1
        z += 4

    #supposition second derivative
    equation = str(6*inequality[0][0][0])+"a"+str(i) + " + 2b"+str(i)+" = 0" 
    result.append(equation)    
    des.append("supposition")
    superMatrix[k][0]=6*inequality[0][0][0]
    superMatrix[k][1]=2
    equation = str(6*inequality[len(inequality)-1][1][0])+"a"+str(i) + " + 2b"+str(i)+" = 0" 
    superMatrix[k+1][4]=6*inequality[len(inequality)-1][1][0]
    superMatrix[k+1][5]=2
    result.append(equation)    
    des.append("supposition")
    result.append("  ")    
    result.append(" final equations ")
    des.append("  ")
    des.append(" iniquality ")
    superMatrix[k][0] = 1
    totalPivoting.a = superMatrix
    totalPivoting.n = len(superMatrix)
    totalPivoting.marcas = [i for i in range(0,totalPivoting.n)]
    aux = totalPivoting.elimination()
    j = 0
    for i in range(0,len(inequality)):
        func = aux[j]*x**3+aux[j+1]*x**2 + aux[j+2]*x+aux[j+3]
        result.append(func)
        des.append(str(inequality[i][0][0])+" <= x <= "+str(inequality[i][1][0]))
        j += 4
            
    table.add_column("equations",result)
    table.add_column("inequality",des)
    
    print(table)
        
cubic()

