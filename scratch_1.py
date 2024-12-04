class csr:
    def create_matrix():
        n = int(input())
        m = int(input())
        val = []
        col_ind = []
        row_ind = [0]
        matrix = list()
        for iterations in range(n):
            matrix += [list(map(int, input().split()))]
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
    if len() != len(csr_matrix[2] - 1):
        return "error, not square"




print(csr_to_normal(csr.create_matrix()))
