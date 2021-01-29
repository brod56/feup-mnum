def cholesky(A):
    #zero
    B = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    C = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    #steps 1 and 3
    for i in range(len(A)):
        B[i][0] = A[i][0]
        C[0][i] = A[0][i]/B[0][0]
        C[i][i] = 1

    #steps 2 and 4
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i >= j:
                B[i][j] = A[i][j] - sum(B[i][k]*C[k][j] for k in range(0,j))
            else:
                C[i][j] = (A[i][j] - sum(B[i][k]*C[k][j] for k in range(0,i)))/B[i][i]

    return B,C


def solve_cholesky(S,B,C):
    X = [0,0,0]
    Y = [0,0,0]
    for i in range(len(Y)):
        Y[i] = (S[i] - sum([B[i][k]*Y[k] for k in range(len(S))]))/B[i][i]
    for i in range(len(X)-1,-1,-1):
        X[i] = (Y[i] - sum([C[i][k]*X[k] for k in range(len(Y))]))/C[i][i]

    return X