from prettytable import PrettyTable

table = PrettyTable()
xn =[1,1.2,1.4,1.6,1.8,2]
fxn =[0.6747,0.8491,1.1214,1.4921,1.9607,2.5258]
derivs =[]
zeros =[]
n = [x for x in range (0,len(xn))]
def newtonInterpolation(actualValues,difference,i,actual):
    if(len(actualValues) == 1):
        derivs.append(actual)
    elif(i==len(actualValues)):
        aux =[]
        for i in range(0,difference+1):
            aux.append(0)
        zeros.append(aux)
        derivs.append(actual)
        newtonInterpolation(actual,difference+1,1,list())
    else:
        
        f =[(actualValues[i]-actualValues[i-1])/(xn[i+difference]-xn[i-1])]
        #print(actualValues[i],"-",actualValues[i-1],"/",xn[i+difference],"-",xn[i-1],"=",f)
        newtonInterpolation(actualValues,difference,i+1,actual+f)
    
newtonInterpolation(fxn,0,1,list())
x = str(fxn[0])
prev = ""
for i in range(0,len(derivs)-1):
    prev = prev +"(x-"+str(xn[i])+")"
    x = x+"+"+str(derivs[i][0])+prev+"\n"
print(x)

table.add_column("xn",xn)
table.add_column("f(xn)",fxn)
for i in range(0,len(derivs)-1):
    table.add_column("deriv "+str(i+1),zeros[i]+derivs[i])
print(table)