#!/usr/bin/env python3
def matrix_transpose(matrix):
    mat3 = []
    for i in range(len(matrix[0])):
        m = []
        for j in range(len(matrix)):
            m.append(matrix[j][i])
        mat3.append(m)
    return mat3
  
