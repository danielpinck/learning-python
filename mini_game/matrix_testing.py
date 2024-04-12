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



# print(len(matrix))

# for i in range(len(matrix)):
#         print(*matrix[i])



def create_walls(liste = create_matrix()):
    matrix_height = len(liste)
    matrix_width = len(liste[0])
    
    
    for i in range(matrix_height):
        for j in range(matrix_width):
            if i == 0:
                liste[i][j] = "1"
            if j == 0:
                liste[i][j] = "1"
            if i == matrix_height-1:
                 liste[i][j] = "1"
            if j == matrix_width-1:
                 liste[i][j] = "1"
    

    return liste

matrix_walls = create_walls()

for i in range(len(matrix_walls)):
        print(*matrix_walls[i])

# print("\U0001F511")
        
# matrix_test = [["0","0","0","0","0","0"],
#           ["0","0","0","0","0","0"],
#           ["0","0","0","0","0","0"],
#           ["0","0","0","0","0","0"],
#           ["0","0","0","0","0","0"],
#           ["0","0","0","0","0","0"]]