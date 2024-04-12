import random

def create_matrix():
    
    height_list = []
    width_length = random.randint(16,20)
    for i in range(random.randint(9,12)):
        width_list = [" "] * width_length
        height_list.append(width_list)


    
    return height_list



def build_walls(liste):
    
    for i in range(len(liste[0])):
        liste[0][i] = "#"
        liste[-1][i] = "#"
    for j in range(len(liste)):
        liste[j][0] = "#"
        liste[j][-1] = "#"

