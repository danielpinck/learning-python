startliste = [5,2,17,3,1,16,12,4,11]
def aufgabe8(liste):
    temp_liste = []
    sublist = []
    while liste:
        for nummer in liste:
            if nummer == min(liste):
                temp_liste.append(nummer)
                liste.remove(nummer)
    liste = temp_liste
    temp_liste = []
    for i in range(len(liste)):
        if liste[i] != liste[i - 1] + 1:
            
            liste.append([liste[i]])
        else:
            liste[-1].append(liste[i])


    print(temp_liste)



    

    return liste
    

print(aufgabe8(startliste))


