import random

def builtMatrix():  # 정사각행렬 생성
    global m
    m = int(input())
    matrix = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            matrix[i][j] += random.random()    # 성분의 범위 설정
    return matrix 

def traceMatrix(matrix):    # 대각합 계산
    tr_matrix = 0
    for i in range(m):
        tr_matrix += matrix[i][i]
    return tr_matrix

X = builtMatrix()
for mat in X:
    print(mat)
print(traceMatrix(X))