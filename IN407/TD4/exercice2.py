matrixA = [[4,0],[0,1]]
matrixB = [[2,1],[0,0]]

def sum_matrix(mA:list[list],mB:list[list]):
    mC = []
    for i in range(len(mA)):
        mC.append([])
        for j in range(len(mA[0])):
            mC[i].append(0)
            mC[i][j] = mA[i][j] + mB[i][j]
    return mC

def sum_matrix_v2(mA:list[list],mB:list[list]):
    return [[mA[i][j]+mB[i][j] for j in range(len(mA[0]))] for i in range(len(mA))]

def check_paire_matrix(matrix:list[list]):
    return [[matrix[i][j] if matrix[i][j] % 2 == 0 else 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

def make_vector(matrix):
    return [elt for vec in matrix for elt in vec]

print(sum_matrix(matrixA, matrixB))
matrixC = sum_matrix_v2(matrixA, matrixB)
print(matrixC)
matrixCP = check_paire_matrix(matrixC)
print(matrixCP)
print(make_vector(matrixCP))