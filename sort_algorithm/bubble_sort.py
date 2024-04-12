
def bubble_num(liste):
    for j in range(len(liste)-1):

        for i in range(len(liste)-1 - j):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste




