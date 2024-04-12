def insertion_sort(liste):
    
    i = 1
    while i < len(liste):
        index = i -1
        temp = liste[i]
        while index >= 0 and liste[index] > temp:
            liste[index + 1] = liste[index]
            index -= 1
        liste[index + 1] = temp
        i += 1
    return liste

