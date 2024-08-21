import math
def complex_sum (A, B):
    real = A[0] + B[0]
    Complex = A[1] + B[1]
    return real, Complex

def complex_subtract (A, B):
    real = A[0] - B[0]
    Complex = A[1] - B[1]
    return real, Complex
def complex_mult(A, B):
    real = (A[0] * B[0]) + (A[1] * B[1] * -1)
    Complex = (A[0]*B[1]) + (A[1]*B[0])
    return real, Complex

def complex_division(A, B):
    real = ((A[0] * B[0]) + (A[1] * B[1])) / (B[0]**2 + B[1]**2 )
    Complex = ((B[0] * A[1]) - (A[0] * B[1])) / (B[0]**2 +B[1]**2)
    return real, Complex

def module(A):
    return(math.sqrt(A[0]**2 + A[1]**2))

def conjugate(A):
    return(A[0],A[1]*-1)

def complex_corte2polar(A):
    p = module(A)
    t = math.atan(A[1]/A[0])
    return p, t
def complex_polar2carte(A):
    a = A[0] * math.acos(A[1])
    b = A[0] * math.asin(A[1])
    return (a, b)  
def complex_phase(A):
    return math.atan(A[1]/A[0])
