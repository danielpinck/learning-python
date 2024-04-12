import random
def width():
    width_list = []
    for i in range(random.randint(8,15)):

        width_list.append("*")
    print(len(width_list))
    return width_list

def create_matrix(list=width()):

    matrix = []
    for i in range(random.randint(5,10)):
    
        matrix.append(list)
    return matrix

matrix_creation = create_matrix()


for i in range(len(matrix_creation)):
        print(*matrix_creation[i])

matrix_test = [["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"]]

def create_walls(matrix):
    matrix_length = len(matrix[0])
    matrix_height = len(matrix)
    
    
    for i in range(matrix_height):
        for j in range(matrix_length):
            if i == 0:
                matrix[i][j] = "1"
            if j == 0:
                matrix[i][j] = "1"
            if i == matrix_height-1:
                 matrix[i][j] = "1"
            if j == matrix_length-1:
                 matrix[i][j] = "1"
    

    return matrix

matrix_walls = create_walls(matrix_test)

for i in range(len(matrix_walls)):
        print(*matrix_walls[i])

# print("\U0001F511")