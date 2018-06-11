import math

gauss = [
        [45,-3,-5,-7,34],
        [7,23,-5,-2,45],
        [-5,-2,67,-8,29],
        [-3,-4,-7,78,79]
        ]
U = list(map(list, gauss)) 

n = len(U)
L = [[0 for x in range(n+1)] for y in range(n)] 

def elimination():
    for k  in range(0,n-1):
        L[k][k] = 1 #doolittle
        L[k][n] = U[k][n]
        for i  in range (k + 1, n):
            multiplicator = U[i][k]/U[k][k]
            L[i][k] = multiplicator
            for j in range (k,n):
                U[i][j] = U[i][j]-(multiplicator*U[k][j])
        L[k+1][k+1] = 1
        L[k+1][n] = U[k+1][n]
    progressiveSustitution()
    democraticSustitution()

def progressiveSustitution():
    n = len(L) -1
    x = [i for i in range(n+1)]
    try:
        x[0] = L[0][n+1]/L[0][0]
    except:
        print ("error division 0 with ",L[n][n+1]," y ",L[n][n])
    for i in range(1,n+1):
        summation = 0
        for p in range(0,i):
            summation = summation + L[i][p]*x[p]
        try:
            x[i]=(L[i][n+1]-summation)/L[i][i]
            U[i][n+1] = x[i]

        except:
            print ("error division 0 with ",(L[i][n+1]-summation)," y  ",L[i][i])
    print("sustitution progre",x)
            
def democraticSustitution():
    n = len(U) -1
    x = [i for i in range(n+1)]
    try:
        x[len(x)-1] = U[n][n+1]/U[n][n]
    except:
        print ("error division 0 with ",U[n][n+1]," y ",U[n][n])
    for i in range(0,n+1):
        summation = 0
        auxi = n - i 
        summation = 0
        for p in range(auxi+1,n+1):
            summation = summation + U[auxi][p]*x[p]
        try:
            x[auxi]=(U[auxi][n+1]-summation)/U[auxi][auxi]
        except:
            print ("error division 0 with ",(U[auxi][n+1]-summation)," y  ",U[auxi][auxi])
    print("final result",x)  

elimination()

print(" chart de U")
for i in U:
    print(i)
print(" chart de L")
for i in L:
    print(i)

