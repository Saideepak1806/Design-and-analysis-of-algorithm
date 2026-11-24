print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    k = n // 2

    A11 = [row[:k] for row in A[:k]]
    A12 = [row[k:] for row in A[:k]]
    A21 = [row[:k] for row in A[k:]]
    A22 = [row[k:] for row in A[k:]]

    B11 = [row[:k] for row in B[:k]]
    B12 = [row[k:] for row in B[:k]]
    B21 = [row[:k] for row in B[k:]]
    B22 = [row[k:] for row in B[k:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    C = [[0] * n for _ in range(n)]

    for i in range(k):
        for j in range(k):
            C[i][j] = C11[i][j]
            C[i][j+k] = C12[i][j]
            C[i+k][j] = C21[i][j]
            C[i+k][j+k] = C22[i][j]

    return C

A = [[1, 7], [3, 5]]
B = [[1, 3], [7, 5]]

result = strassen(A, B)

print("\nResult Matrix:")
for row in result:
    print(row)