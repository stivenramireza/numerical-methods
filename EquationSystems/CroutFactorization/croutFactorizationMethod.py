
a = [
        [36,3,-4,5,-20],
        [5,-45,10,-2,69],
        [6,8,57,5,96],
        [2,3,-8,-42,-32]
        ]
n = len(a)
L = [[0 for x in range(n+1)] for y in range(n)] 
U = [[0 for x in range(n+1)] for y in range(n)] 
def initialization(matrix):
    for i in range(0,n):
        matrix[i][i] = 1

def crout():
    for k in range (0,n):
        sum1 = 0
        for p in range (0,k):
            sum1 = sum1 + L[k][p]*U[p][k]
        L[k][k] = a[k][k] - sum1
        for i in range (k+1,n):
            sum2 = 0
            for p in range (0,k):
                sum2 = sum2 + L[i][p]*U[p][k]
            
            L[i][k] = (a[i][k] - sum2)/U[k][k]
        for j in range (k+1,n):
            sum3 = 0
            for p in range (0,k):
                sum3 =  sum3 + L[k][p]*U[p][j]
            U[k][j] = (a[k][j] - sum3)/L[k][k]
        L[k][n]=a[k][n]

def progressiveSustitution():
    n = len(L) -1
    x = [i for i in range(n+1)]
    try:
        x[0] = L[0][n+1]/L[0][0]
    except:
        print ("error division 0 with ",L[n][n+1]," y ",L[n][n])
    for i in range(0,n+1):
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
            
initialization(U)
crout()
progressiveSustitution()
democraticSustitution()

print("L")
for i in L:
    print(i)
print("U")
for i in U:
    print(i)