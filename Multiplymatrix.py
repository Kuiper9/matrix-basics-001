import sys
input = sys.stdin.readline

def buildMatrix(n, m):
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    return matrix

def multiplyMatrix(mat_A, mat_B, n, m,  k):
    mul_matrix = [[0] * k for _ in range(n)]
    x = 0
    y = 0
    for i in range(n):
        for j in range(k):
            for l in range(m):
                mul_matrix[i][j] += mat_A[i][l] * mat_B[l][j]
    return mul_matrix

#mat_A = N * M, mat_B = M * K
N, M = map(int, input().strip().split())
A = buildMatrix(N, M)
M, K = map(int, input().strip().split())
B = buildMatrix(M, K)
result = multiplyMatrix(A, B, N, M, K)
for row in result:
    print(*row, sep=' ')