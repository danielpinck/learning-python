import random
def create_matrix():
    sweeper_list = []
    for i in range(6):
    
        sweeper_sublist= ["X","X","X","X","X","X"]
        random.seed(random.randint(1,500))
        for i in range(random.randint(1,3)):
            
            sweeper_sublist[random.randint(0,5)] = 0
    
        sweeper_list.append(sweeper_sublist)

            
    # for sublist in sweeper_list:
    #     print(*sublist)
    return sweeper_list

matrix = create_matrix()
# for sublist in range(len(matrix)):
#     print(*matrix[sublist])

# matrix = [[0,"X",0,"X","X",0],
#           ["X",0,"X",0,"X","X"],
#           [0,"X",0,"X",0,"X"],
#           ["X",0,0,"X","X",0],
#           ["X",0,"X",0,"X","X"],
#           [0,0,"X",0,0,"X"]]


for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 0:
            # rechts, gleiche Zeile
            if j+1 < len(matrix) and matrix[i][j+1] == "X":
                matrix[i][j] += 1
            # links, gleiche Zeile
            if j > 0 and matrix[i][j-1] == "X":
                matrix[i][j] += 1
            # zeile darunter
            if i+1 < len(matrix) and matrix[i+1][j] == "X":
                matrix[i][j] += 1
            # links, zeile darunter
            if j > 0 and i+1 < len(matrix) and matrix[i+1][j-1] == "X":
                matrix[i][j] += 1
            # rechts, zeile darunter
            if j+1 < len(matrix) and i+1 < len(matrix) and matrix[i+1][j+1] == "X":
                matrix[i][j] += 1
            # zeile darüber
            if i > 0 and matrix[i-1][j] == "X":
                matrix[i][j] += 1
            # links, zeile darüber
            if j > 0 and i > 0  and matrix[i-1][j-1] == "X":
                matrix[i][j] += 1
            # rechts, zeile darüber
            if j+1 < len(matrix)  and i > 0 and matrix[i-1][j+1] == "X":
                matrix[i][j] += 1

for i in range(len(matrix)):
        print(*matrix[i])


