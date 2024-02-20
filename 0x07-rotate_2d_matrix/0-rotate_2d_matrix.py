#!/usr/bin/python3
""""""


def rotate_2d_matrix(matrix):
    """"""
    dim = len(matrix)

    for i in range(dim):
        for j in range(i+1, dim):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for col in range(dim//2):
        for row in range(dim):
            temp = matrix[row][col]
            matrix[row][col] = matrix[row][dim-col-1]
            matrix[row][dim-col-1] = temp
