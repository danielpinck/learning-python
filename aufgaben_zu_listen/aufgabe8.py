startliste = [5,2,17,3,1,16,12,4,11]
def aufgabe8(liste):
    temp_liste = []
    sublist = []
    while liste:
        for nummer in liste:
            if nummer == min(liste):
                temp_liste.append(nummer)
                liste.remove(nummer)
    #liste = temp_liste
    for i in range(len(temp_liste)):
        if temp_liste[i] != temp_liste[i - 1] + 1:
            sublist = [temp_liste[i]]
            liste.append(sublist)
        else:
            sublist.append(temp_liste[i])


    print(temp_liste)



    

    return liste
    

print(aufgabe8(startliste))


