import random

def buildMatrix(M, N):  # 0이상 1미만의 실수를 성분으로 갖는 m x n크기의 행렬 X생성
    X = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            X[i][j] += random.random()
    return X

def printMatrix(x):
    for mat in x:
        print(mat)

def isMatrixEqual(matrix_A, matrix_B):    # 두 행렬이 얼마나 비슷한지 퍼센트로 반환
    total_value = len(matrix_A) * len(matrix_A[0])
    equal_value = 0
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[i])):
            equal_value += 1 if matrix_A[i][j] == matrix_B[i][j] else 0
    percentage = equal_value / total_value * 100
    print('{:.20f}%'.format(percentage))    # 소수점 5자리까지만 출력

m, n = map(int, input().strip().split())
A = buildMatrix(m, n)
B = buildMatrix(m, n)
printMatrix(A)
printMatrix(B)
isMatrixEqual(A, B)