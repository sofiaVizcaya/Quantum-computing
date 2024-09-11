import math
def add_vector(A,B):
    C = []
    for i in range(0, len(A)):
        C.append(complex_sum(A[i], B[i]))
    return C
def sub_vector(A,B):
    C = []
    for i in range(0, len(A)):
        C.append(complex_subtract(A[i], B[i]))
    return C
def complex_inv_vect(A):
    C = []
    for i in range(0,len(A)):
        a = -1*A[i][0],-1*A[i][1]
        C.append(a)
    return C
def VectTimesScalar (A,c):
    B = []
    for i in range (0, len(A)):
        a = (A[i][0]*c, A[i][0]*c)
        B.append(a)
    return B
def verifyComplexMatrixSum(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return True
    else :
        return False
def complexMatrixSum(A, B):
    C = []
    if verifyComplexMatrixSum(A, B):
        for i in range (0, len(A)):
            D = []
            for j in range (0, len(A[0])):
                D.append(complex_sum(A[i][j] ,B[i][j]))
            C.append(D)
            
    return C
def addInverseMat(A):
    C = []
    for i in range(0, len(A)):
        D = []
        for j in range (0, len(A[0])):
            b = (A[i][j][0] * -1), (A[i][j][1] * -1)
            D.append(b)
        C.append(D)
    return C
def multiplyScalarMatrix(A, c):
    B = []
    for i in range(0, len(A)):
        J = []
        for j in range(0, len(A[0])):
            b = A[i][j][0] * c, A[i][j][1] * c
            J.append(b)
        B.append(J)
    return B
def transposed_matrix(A):
    B = []
    for i in range(0, len(A)):
        J = []
        for j in range (0, len(A[0])):
            b = A[j][i]
            J.append(b)
        B.append(J)
    return B
def transposed_vector(A):
    return A
def conjugate_matrix(A):
    B = []
    for i in range (0, len(A)):
        J = []
        for j in range(0, len(A[0])):
            b = conjugate(A[i][j])
            J.append(b)
        B.append(J)
    return B
def conjugate_vector(A):
    B = []
    for i in range(0, len(A)):
        B.append(conjugate(A[i]))
    return B
def verfProductMatrix(A, B):
    if len(A[0]) == len(B):
        return True
    else:
        return False
def verfActionMatrix(A , x):
    if (len(A[0]) == len(A)) and len(A[0] == len(x)):
        return True
    else:
        return False
def complexMatrixMultiply(A, B):
    C = []
    for i in range (0, len(A)):
        C.append([])
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i].append(complexMatrixComplement(A, B, i, j))
    return (C)
def matrix_mult_complex(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        raise ValueError("Número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
    result = [[(0, 0) for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            sum = (0, 0)
            for k in range(cols1):
                # Multiplicar el elemento de la fila i y columna k de matrix1
                # con el elemento de la fila k y columna j de matrix2
                product = complex_mult(matrix1[i][k], matrix2[k][j])
                # Sumar el producto al resultado
                sum = complex_sum(sum, product)
            result[i][j] = sum
    return result
def complexInternalProduct(u, v):
    u, v = list(u), list(v)
    Answer = [0, 0]
    print(len(u))
    for i in range(0, len(u)):
        X = complex_mult(u[i], v[i])
        Answer = complex_sum(Answer, X)
    return Answer
def actionMatrixVect(A,x):
    C = []
    if verfActionMatrix(A , x):
        for i in range(0,len(x)):
            a ,b = 0,0
            for j in range(0, len(x)):
                a = (A[j][i][0] * x[j][0]) + a
                b = (A[j][i][1] * x[j][1]) + b
                c = (a, b)
            C.append(c)
        return C
def innerProductVect(A,B):
    C = []
    for i in range(0 , len(A)):
        b = (A[i][0] * B[i][0]), (A[i][1] *B[i][1])
        C.append(b)
    return C

def NormVector(A):
    C = []
    a, b = 0, 0
    for i in A:
        a = a + i[0] ** 2
        b = b + i[1] ** 2
    c = math.sqrt(a + b)
    return c

    
def DistanVector(A,B):
    C = []
    return sub_vector(A, B)

def hermitianMatCheck(A):
    Id = []
    for i in range (0,len(A)):
        J = [] 
        for j in range(0,len(A)):
            if i == j :
                J.append(1)
            else:
                J.append(0)
        Id.append(J)
    B = transposed_matrix(A)
    C = matrix_mult_complex(A, B)
    if Id == C:
        return True
    else:
        return False
