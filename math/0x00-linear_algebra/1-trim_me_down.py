matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
lenght=len(matrix)
for i in range(lenght):
    the_middle.append(matrix[i][2:4])
print("The middle columns of the matrix are: {}".format(the_middle))
