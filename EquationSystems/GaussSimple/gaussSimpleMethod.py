import numpy as np
import math

gauss = [
        [1,1/2,1/3,1],
        [1/2,1/3,1/4,0],
        [1/3,1/4,1/5,0],
        ]            

n = len(gauss)

def roundingCut(value,decimals):
     return math.floor(value*10**decimals)/10**decimals
     #return value

def elimination():
    
    for k  in range(0,n-1):
        for i  in range (k + 1, n):
            try:
                multiplicator =  gauss[i][k]/gauss[k][k]
            except:
                print ("Error in division 0 with " , gauss[i][k]," y ",gauss[k][k])
            for j in range (k,n + 1):
                gauss[i][j] =  gauss[i][j]-(multiplicator*gauss[k][j])

    sustitution()

def sustitution():
    n = len(gauss) -1
    x = [i for i in range(n+1)]
    try:
        x[len(x)-1] =  gauss[n][n+1]/gauss[n][n]
    except:
        print ("Error in division 0 with ",gauss[n][n+1]," y ",gauss[n][n])
    for i in range(0,n+1):
        summation = 0
        auxi = n - i 
        summation = 0
        for p in range(auxi+1,n+1):
            summation = summation + gauss[auxi][p]*x[p]
        try:
            x[auxi]= (gauss[auxi][n+1]-summation)/gauss[auxi][auxi]
        except:
            print ("Error in division 0 with ",(gauss[auxi][n+1]-summation)," y  ",gauss[auxi][auxi])
    print(x)
            
elimination()
for i in gauss:
    print(i)

