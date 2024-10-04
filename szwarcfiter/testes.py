# 03/10/2024
matrix_a = [[1,2,3], [4,2,3], [1,5,1]]

matrix_b = [[2,1,3], [3,1,5], [2,3,1]]

new_matrix = [[1, 2, 3], [9, 0, 0], [0, 0, 0]]

print(f'{len(new_matrix[0])} - len', \
        new_matrix[0])

for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        # setou-se len(matrix_a[0]) em zero
        # porque todas as colunas têm mesmo tamanho
        new_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

for i in range(len(new_matrix)):
    for j in range(len(new_matrix[0])):
        print(new_matrix[i][j])
