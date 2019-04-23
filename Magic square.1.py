import numpy
import time

size = (3,3)

matrix = numpy.zeros(shape=size)

matrix[0][0] = 2
matrix[2][2] = 8 


def winner(matrx):
    print("==================")
    print(matrix)
    print("Success!!")

def check_matrix(matrix):
    for row in matrix:
        if sum(row) != 15:
            return False
    for i in range(0, 3):
        col = matrix[:, i]
        print(col)
        if sum(col) != 15:
            return False
    if matrix[0][0] + matrix[1][1] + matrix[2][2] != 15:
        return False
    if matrix[0][2] + matrix[1][1] + matrix[2][0] != 15:
        return False
    if len(numpy.unique(matrix)) != size[0] * size[1]:
        return False
    return True

def check(x, y):
    for item in dont_handle:
        if item == [y, x]:
            return True
    return False


indexes = []
last_to_check = []
indexes_cord = {}
dont_handle = []

for i in range(0, size[0]):
    for j in range(0, size[1]):
        indexes.append([i, j])
        indexes_cord[f"{[i,j]}"] = len(indexes) - 1
        if matrix[i][j] != 0:
            dont_handle.append([i,j])
        
        else:
            last_to_check = [i, j]

while True:
    print(matrix)
    for y in range(0, size[0]):
        for x in range(0, size[1]):
            if check(x, y):
                continue
            index = indexes_cord[f"{[y,x]}"]
            if matrix[y][x] == 10:
                index = index - 1
                new_i = indexes[index]
                while check(new_i[1], new_i[0]):
                    index = index - 1
                    new_i = indexes[index]
                matrix[new_i[0]][new_i[1]] += 1
                matrix[y][x] = 1
            elif [y, x] == last_to_check:
                matrix[y][x] += 1
            if check_matrix(matrix):
                winner(matrix)
                exit()
            

    
            




    