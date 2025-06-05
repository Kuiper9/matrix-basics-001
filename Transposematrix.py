import random

def buildMatrix():
    m, n = map(int, input().split())
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] += random.randint(0, 10)
    return matrix

def trasposeMatrix(matrix):
    transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix

def printMatrix(matrix_a, matrix_b):
    print('Before :', *matrix_a, sep='\n')
    print('After :', *matrix_b, sep='\n')

A = buildMatrix()
B = trasposeMatrix(A)
printMatrix(A, B)

#전치 예시
# a = [
#     [10, 11, 12, 13],
#     [20, 21, 22, 23],
#     [30, 31, 32, 33]
# ]
# b = [
#     [10, 20, 30],
#     [11, 21, 31],
#     [12, 22, 32],
#     [13, 23, 33]
# ]