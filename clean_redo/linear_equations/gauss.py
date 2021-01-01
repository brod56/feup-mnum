def gauss(matrix):
    for i in range(len(matrix)): #elem da diagonal principal
        div_factor = matrix[i][i]
        for k in range(i, len(matrix[i])):
            matrix[i][k] /= div_factor #tornar cof unitário
            
        for j in range(i+1, len(matrix)):
            sub = matrix[j][i]
            for l in range(i, len(matrix[i])):
                matrix[j][l] -= sub*matrix[i][l] #zerar elementos abaixo
    return matrix
