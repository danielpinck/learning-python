verschieben_liste = [1,2,4,3,5,6,7,8]

def aufgabe6(liste):
    



    for i in range(len(verschieben_liste)):
        for j in range(len(verschieben_liste)-(len(verschieben_liste)-1)):

                temp = verschieben_liste[j]
                verschieben_liste[j] = verschieben_liste[i]
                verschieben_liste[i] = temp
    return liste

print(aufgabe6(verschieben_liste))
