import math
import numpy as np
           
a = [ [-7,2,-3,4,-12],
        [5,-1,14,-1,13],
        [1,9,-7,13,31],
        [-12,13,-8,-4,-32]
        ]

n = len(a)
marks = [i for i in range(0,n)]

def changeRows(majorRow,k):
    for i in range(0,len(a)+1):
        aux = a[k][i]
        a[k][i] = a[majorRow][i]
        a[majorRow][i]= aux
    
def changeColumns(majorColumn,k):
    aux = marks[k]
    marks[k] = marks[majorColumn]
    marks[majorColumn] = aux
    for j in range(0,len(a)):
        aux = a[j][k]
        a[j][k] = a[j][majorColumn]
        a[j][majorColumn] = aux
        
def totalPivoting(k):
    major = 0
    majorRow = k
    majorColumn = k
    for r in range(k,n):
        for s in range (k,n):
            if (math.fabs(a[r][s]) > major):
                major = math.fabs(a[r][s])
                majorRow = r
                majorColumn = s
        
    if(major == 0):
        print("division 0")
        return;
    else:
        if(majorRow != k):
            changeRows(majorRow,k)
        if(majorColumn != k):
            changeColumns(majorColumn,k)
    
def elimination():
    for k  in range(0,n-1):
        totalPivoting(k)
        for i  in range (k + 1, n):    
            multiplicator = a[i][k]/a[k][k]
            for j in range (k,n + 1):
                a[i][j] = a[i][j]-(multiplicator*a[k][j])
        

    sustitution()

def sustitution():
    n = len(a) -1
    x = [i for i in range(n+1)]
    x[len(x)-1] = a[n][n+1]/a[n][n] 
    for i in range(0,n+1):
        summation = 0
        auxi = n - i 
        summation = 0
        for p in range(auxi+1,n+1):
            summation = summation + a[auxi][p]*x[p]
        x[auxi]=(a[auxi][n+1]-summation)/a[auxi][auxi]
    marks.reverse()
    x.reverse()
    for i in range(0,len(x)):
        print("X",marks[i]," =",x[i])

elimination()
for i in a:
    print(i)



