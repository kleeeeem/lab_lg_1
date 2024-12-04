class CSR:
    def __init__(self, n: int, m: int, matrix: list[list]):
        val = []
        col_ind = []
        row_ind = [0]
        for i in range(n):
            counter = 0
            for j in range(m):
                if matrix[i][j] != 0:
                    val.append(matrix[i][j])
                    col_ind.append(j)
                    counter += 1
            row_ind.append(row_ind[i] + counter)
        return [val, col_ind, row_ind]


def csr_to_normal(csr_matrix):
    col_ind = csr_matrix[1]
    row_ind = csr_matrix[2]
    print(max(col_ind))
    print(len(row_ind))
    matrix = [[0 for i in range(max(col_ind) + 1)] for j in range(len(row_ind) - 1)]
    val = csr_matrix[0]
    for i in range(len(val)):
        col = col_ind[i]
        row = 0
        for j in range(len(row_ind) - 1):
            if i >= row_ind[j] and i < row_ind[j+1]:
                row = j
        matrix[row][col] = val[i]
    return matrix



def determinant(csr_matrix):
    normal_matrix = csr_to_normal(csr_matrix)
    determ = 0
    if len(normal_matrix) != len(normal_matrix[0]):
        return "error, not square"
    if len(normal_matrix) == 2:
        determ = normal_matrix[0][0] * normal_matrix[1][1] - normal_matrix[1][0] * normal_matrix[0][1]
    else:
        for i in range(len(normal_matrix[0])):
            determ += 0


n, m = map(int, input().split())
matrix = [list(map(float, input().split())) for i in range(n)]
csr = CSR(n, m, matrix)
print(csr_to_normal(csr.create_matrix()))
