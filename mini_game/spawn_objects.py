import random as ra
def spawn_object(matrix):
    x = len(matrix)
    y = len(matrix[0])

    player_sprite = "@"

    matrix[ra.randrange(1, x-1)][ra.randrange(1, y-1)] = player_sprite

    return player_sprite