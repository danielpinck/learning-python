import random


def aufgabe1(elemente,num_range):
    random_liste = []
    
    for i in range(elemente):
        random_liste.append(random.randint(1,num_range))
    
    return random_liste