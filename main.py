import numpy as np

Square = np.array([2, 0, 0, 0, 0, 1, 4, 0, 0])

t = -1
rules = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]


# Create the matrix that it will use to calculate the
Matrix = []
for x in rules:
    row = []
    for index in range(len(Square)):
        if index in x:
            row.append(1)
        else:
            row.append(0)
    row.append(t)
    Matrix.append(row)

# Code here calculates the vectors
vectors = np.array([])
for x in rules:
    values = []
    for index in x:
        values.append(Square[index])
    vectors = np.append(vectors, -1 * sum(values))

Matrix = np.array(Matrix)
m = np.linalg.pinv(Matrix).dot(vectors)
import pdb

pdb.set_trace()
index = 0

for i in range(len(Square)):
    if Square[i] == 0:
        Square[i] = round(m[index], 2)
        index += 1


x1 = Square[0]
x2 = Square[1]
x3 = Square[2]
x4 = Square[3]
x5 = Square[4]
x6 = Square[5]
x7 = Square[6]
x8 = Square[7]
x9 = Square[8]

print(m)

print("{}|{}|{}".format(x1, x2, x3))
print("{}|{}|{}".format(x4, x5, x6))
print("{}|{}|{}".format(x7, x8, x9))
print("Total: {}".format(round(m[-1], 0)))
