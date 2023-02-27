def search_2d_matrix(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][0] > target:
            continue
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return False

    return False

def search_2d_matrix_2(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][-1] < target:
            continue
        elif target in matrix[i]:
            return True

        elif matrix[i][0] > target:
            return False
            

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 7

print(search_2d_matrix_2(matrix, target))