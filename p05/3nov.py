import math

#####################################################
#SISTEMAS LINEARES

def khalestky(A,b):
    # TO BE CONTINUED
    
    # U diagonal principal 1
    for i in range(len(A)):
        U[i][i] = 1
        
    # U triangular inferior
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i > j:
                U[i][j] = 0
    
    # L triangular superior
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i < j:
                L[i][j] = 0
    
    for i in range(len(A)):
        L[i][0] = A[i][0]
        
    for i in range(len(A)):
        U[0][i] = A[0][i] / B[0][0]
        
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i < j:
                continue
            L[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(1,j))
            
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i >= j:
                continue
            U[i][j] = (A[i][j] - sum(L[i][k]*U[k][j] for k in range(1,i))) / L[i][i]
            
    print("acabar isto...")    
        
########################################################
# INTEGRAIS
    
def trapezios(f,a,b,n):
    h = (b-a)/n
    return h/2 * ( f(a) +f(b) + 2*sum(f(a + k*h) for k in range(1,n)) )

def simpson(f,a,b,n):
    h = (b-a)/n
    return h/3 * ( f(a) + f(b) + 4*sum(f(a + k*h) for k in range(1,n,2))
                  + 2* sum(f(a + k*h) for k in range(2,n,2)))
    
def qc_trapezios(f,a,b,n): #duplicar n até Qc cerca de 4
    S = []
    for i in range(3):
        S.append(trapezios(f,a,b,n * (2**i)))
    return (S[1]-S[0])/(S[2]-S[1])


def qc_simpson(f,a,b,n): #duplicar n até Qc cerca de 16
    S = []
    for i in range(3):
        S.append(simpson(f,a,b,n * (2**i)))
    return (S[1]-S[0])/(S[2]-S[1])


def erro_trapezios(f,a,b,n):
    S = []
    for i in range(3):
        S.append(trapezios(f,a,b,n * (2**i)))
    return (S[2] - S[1]) / 3
    

def erro_simpson(f,a,b,n):
    S = []
    for i in range(3):
        S.append(simpson(f,a,b,n * (2**i)))
    return (S[2] - S[1]) / 15
    

f = lambda x: math.sin(x) / x**2
a = math.pi/2
b = math.pi
n = 4
print(trapezios(f,a,b,n))
print(simpson(f,a,b,n))
print("----------")

print(qc_trapezios(f,a,b,n)) # 3.98, não duplicar
print(qc_trapezios(f,a,b,2*n)) # 3.99, sem diferença
print(erro_trapezios(f,a,b,2*n))
print("-----------")

print(qc_simpson(f,a,b,n)) # 14.36, necessário duplicar
print(qc_simpson(f,a,b,2*n)) # 15.51, arredonda, ok
print(erro_simpson(f,a,b,2*n))
print("------------")
    