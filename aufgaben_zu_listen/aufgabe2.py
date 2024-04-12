def aufgabe2(liste):
    

    mittelwert = 0
    for i in range(len(liste)):
        mittelwert += liste[i]
    mittelwert = mittelwert/len(liste)
    print(liste)
    
    return mittelwert, liste
