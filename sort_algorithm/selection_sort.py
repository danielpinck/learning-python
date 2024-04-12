def selection_sort(liste):
    i = 0
    while i <= len(liste)-2:
        minindex = i 
        j = i + 1
        while j <= len(liste) -1:
            if liste[j] < liste[minindex]:
                minindex = j
            j += 1
        temp = liste[i]
        liste[i] = liste[minindex]
        liste[minindex] = temp
        i += 1
    return liste
