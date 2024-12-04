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


    def csr_to_normal(self):
        col_ind = self.col_ind
        row_ind = self.row_ind
        matrix = [[0 for i in range(max(col_ind) + 1)] for j in range(len(row_ind) - 1)]
        val = self.val
        for i in range(len(val)):
            col = col_ind[i]
            row = 0
            for j in range(len(row_ind) - 1):
                if i >= row_ind[j] and i < row_ind[j+1]:
                    row = j
            matrix[row][col] = val[i]
        return matrix



    def determinant(self, matrix):
        normal_matrix = CSR.csr_to_normal(self)
        determ = 0
        if len(normal_matrix) != len(normal_matrix[0]):
            return "error, not square"
        if len(normal_matrix) == 1:
            return normal_matrix[0][0]
        else:
            col = -1
            for i in range(len(normal_matrix[0])):
                col += 1
                for j in range(len(normal_matrix)):
                    new_matrix = normal_matrix[:j] + normal_matrix[j + 1:]
                    determ += normal_matrix[i] * CSR.determinant(self, new_matrix)




my_n, my_m = map(int, input().split())
my_matrix = [list(map(float, input().split())) for i in range(my_n)]
csr = CSR(my_n, my_m, my_matrix)
csr.determinant()
print(my_matrix.__init__())
