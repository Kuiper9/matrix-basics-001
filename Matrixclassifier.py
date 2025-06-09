import sys

def buildMatrix():  # m x m크기, 정수 성분을 갖는 정사각행렬 생성
    m = int(input())
    X = []
    for i in range(m):
        row = list(map(int, input().strip().split()))
        if len(row) != m:    # 행렬의 크기를 벗어난 입력값이 감지될 경우 프로그램 종료
            print('Error.')
            sys.exit(1)
        try:
            row = [int(x) for x in row]
        except ValueError:  # 입력값이 정수가 아닐 경우 프로그램 종료
            print('Error.')
            sys.exit(1)
        X.append(row)
    return X

def matrixClassifier(matrix):
    m = len(matrix)
    trace_value = 0    # 대각합
    trace_1_count = 0   # 주대각성분이 모두 1인지 검사
    count_zero = 0    # 주대각성분을 제외한 나머지 성분이 모두 0인지 검사
    transposed = [[0] * m for _ in range(m)]   # matrix의 전치
    for i in range(m):
        trace_value += matrix[i][i]
        if matrix[i][i] == 1:
            trace_1_count += 1
        for j in range(m):
            if i != j:
                if matrix[i][j] == 0:
                    count_zero += 1
            transposed[i][j] = matrix[j][i]
    minus_matrix = [[n * (-1) for n in row] for row in transposed]    # transposed * -1

    if matrix == minus_matrix:
        return 'skew-symmetric matrix'
    if transposed == matrix:
        if count_zero == (m ** 2) - m:
            if trace_1_count == m:
                return 'identity matrix and symmetric matrix'
            else:
                return 'diagonal matrix and symmetric matrix'
        else:
            return 'symmetric matrix'
    else:
        return 'not symmetric matrix'

A = buildMatrix()
print(*A, sep='\n')
print(matrixClassifier(A))