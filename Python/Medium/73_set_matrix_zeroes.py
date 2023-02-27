def matrix_zeroes(mat):
    rows = []
    cols = []

    for i in range(len(mat)):
        
        if 0 in mat[i]:
            rows.append(i)
        for j in range(len(mat[0])):
            if matrix[i][j] == 0:
                cols.append(j)


    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i in rows:
                mat[i][j] = 0
            elif j in cols:
                mat[i][j] = 0

    return mat



matrix = [[1,1,1], [1,0,1], [1,1,1]]
print(matrix_zeroes(matrix))