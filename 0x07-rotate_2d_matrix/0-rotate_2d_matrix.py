#!/usr/bin/python3
"""
Module for rotating a matrix 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    rotating a matrix 90 degrees clockwise.
    """
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
