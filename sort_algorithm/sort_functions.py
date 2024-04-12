import random
from datetime import datetime
def time_function(sort_function, *args, **kwargs):
    before = datetime.now()

    sort_function(*args, **kwargs)
    after = datetime.now()
    time_diff = after - before

    return time_diff
    

def fill_list(elements, liste, num_range, random_seed):
    
    
    for i in range(elements):
        liste.append(random.randint(1,num_range))
    return liste, random_seed

def bubble_num(liste):
    for j in range(len(liste)-1):

        for i in range(len(liste)-1 - j):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste

def bubble_while(liste):
    tausch = True
    while tausch:
        tausch = False
        i = 0
        while i < len(liste)-1:

            
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                
                tausch = True
            i += 1
    return liste

def insertion_sort(liste):
    
    i = 1
    while i < len(liste):
        index = i -1
        temp = liste[i]
        while index >= 0 and liste[index] > temp:
            liste[index + 1], liste[index] = liste[index], liste[index + 1] 
            index -= 1
        
        i += 1
    return liste

def selection_sort(liste):
    i = 0
    while i <= len(liste)-2:
        minindex = i 
        j = i + 1
        while j <= len(liste) -1:
            if liste[j] < liste[minindex]:
                minindex = j
            j += 1
        liste[i], liste[minindex] = liste[minindex], liste[i]
        i += 1
    return liste

def shell_sort(liste):
    h = 1
    while h < len(liste) // 2:
        h = 2 * h + 1

    while h >= 1:
        i = h

        while i <= len(liste) - 1:
            index = i - h 

            while index >= 0 and liste[index] > liste[index + h]:
                liste[index + h], liste[index] = liste[index], liste[index + h]
                index = index - h
            i += 1
        h = h // 2

    return liste
