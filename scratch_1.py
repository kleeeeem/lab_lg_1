class csr:
    def create_matrix():
        m = int(input())
        n = int(input())
        val = []
        trace = 0
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


print(csr.create_matrix())
