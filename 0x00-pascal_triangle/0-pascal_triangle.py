#!/usr/bin/python3

def pascal_triangle(n)
    if type(n) is not int:
        raise TypeError("n must be an integer")
    matrix = []
    if n <= 0:
        return matrix
    for i in range(n):
        arr = []
        for j in range(i+1):
            if j == 0:
                arr.append(1)
            elif j == i:
                arr.append(1)
            else:
                arr.append(matrix[i-1][j-1] + matrix[i-1][j])
        matrix.append(arr)
    return matrix
