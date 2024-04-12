import random as ra, keyboard, os
from create_room import *
from spawn_objects import *

matrix = create_matrix()
build_walls(matrix)
spawn_object(matrix)

for i in range(len(matrix)):
    print(*matrix[i])
