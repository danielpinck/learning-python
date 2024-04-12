def aufgabe3(liste):
    neue_liste = []
    
    for i in range(len(liste)):
        summe = 0
        for j in str(liste[i]):
            summe += int(j)
        neue_liste.append(summe)
    print(liste)
    return neue_liste
