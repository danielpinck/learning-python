import random as ra
def spawn_object(matrix):
    x = len(matrix)
    y = len(matrix[0])

    spawn_player = "@"

    matrix[ra.randrange(1, x-1)][ra.randrange(1, y-1)] = spawn_player