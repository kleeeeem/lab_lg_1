class CSR:
    def __init__(self, n: int, m: int, matrix: list[list]):
        self.val = []
        self.col_ind = []
        self.row_ind = [0]
        for i in range(n):
            counter = 0
            for j in range(m):
                if matrix[i][j] != 0:
                    self.val.append(matrix[i][j])
                    self.col_ind.append(j)
                    counter += 1
            self.row_ind.append(self.row_ind[i] + counter)
    def trace(self):
        trace = 0
        val = self.val
        col_ind = self.col_ind
        row_ind = self.row_ind
        if max(col_ind) == len(row_ind) - 1:
            return "error, not a square matrix"
        for i in range(len(val)):
            if (i >= row_ind[col_ind[i]]) and (i < row_ind[col_ind[i] + 1]):
                trace += val[i]
        return trace
    def display_element(self, row, col):
        row1 = row - 1
        col1 = col - 1
        val = self.val
        col_ind = self.col_ind
        row_ind = self.row_ind
        for i in range(len(val)):
            if (col_ind[i] == col1) and (i >= row_ind[row1]) and (i < row_ind[row1 + 1]):
                return val[i]
    def csr_to_normal(self):
        col_ind = self.col_ind
        row_ind = self.row_ind
        matrix = [[0 for i in range(max(col_ind) + 1)] for j in range(len(row_ind) - 1)]
        val = self.val
        for i in range(len(val)):
            col = col_ind[i]
            row = 0
            for j in range(len(row_ind) - 1):
                if (i >= row_ind[j]) and (i < row_ind[j + 1]):
                    row = j
            matrix[row][col] = val[i]
        return matrix
n, m = map(int, input().split())
matrix = [list(map(float, input().split())) for i in range(n)]
csr = CSR(n, m, matrix)
print(csr.csr_to_normal())
print(csr.trace())
print(csr.display_element(1,2))
#meow