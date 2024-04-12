
def sortiereTelefon(liste, index):

    for i in range(len(liste)-1):
        for j in range(len(liste)-1):
            if liste[j][index] > liste[j+1][index]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
