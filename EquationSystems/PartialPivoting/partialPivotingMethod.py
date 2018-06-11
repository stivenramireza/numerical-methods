import math
import numpy as np

gauss = [
        [-7,2,-3,4,-12],
        [5,-1,14,-1,13],
        [1,9,-7,13,31],
        [-12,13,-8,-4,-32]
        ]

n = len(gauss)

def changeRows(majorRow,k):
    for i in range(0,len(gauss)+1):
        aux = gauss[k][i]
        gauss[k][i] = gauss[majorRow][i]
        gauss[majorRow][i]= aux

def pivoting(k):
    major = math.fabs(gauss[k][k])
    majorRow = k
    for s in range(k+1,n):
        if (math.fabs(gauss[s][k]) > major):
            major = math.fabs(gauss[s][k])
            majorRow = s
        
    if(major == 0):
        print("division 0")
        return;
    elif(majorRow != k):
        changeRows(majorRow,k)

def elimination():
    for k  in range(0,n-1):
        pivoting(k)
        for i  in range (k + 1, n):
            multiplicator = gauss[i][k]/gauss[k][k]
            for j in range (k,n + 1):
                gauss[i][j] = gauss[i][j]-(multiplicator*gauss[k][j])

    sustitution()

def sustitution():
    n = len(gauss) -1
    x = [i for i in range(n+1)]
    x[len(x)-1] = gauss[n][n+1]/gauss[n][n]
    print(x[len(x)-1])
    
    for i in range(0,n+1):
        summation = 0
        auxi = n - i 
        summation = 0
        for p in range(auxi+1,n+1):
            summation = summation + gauss[auxi][p]*x[p]
        x[auxi]=(gauss[auxi][n+1]-summation)/gauss[auxi][auxi]
    print(x)
            

elimination()
for i in gauss:
    print(i)

