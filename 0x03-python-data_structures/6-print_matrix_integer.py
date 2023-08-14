#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    else:
        for i in matrix:
            f_list = " ".join("{:d}".format(j) for j in i)
            print(f_list)
