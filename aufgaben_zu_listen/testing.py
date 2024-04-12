startliste = [5, 2, 17, 3, 1, 16, 12, 4, 11]

def aufgabe8(liste):
    temp_liste = []
    neue_liste = []
    
    # Sorting the list
    liste.sort()

    sublist = []
    for nummer in liste:
        if not sublist or nummer == sublist[-1] + 1:
            sublist.append(nummer)
        else:
            temp_liste.append(sublist)
            sublist = [nummer]
    
    # Append the last sublist
    temp_liste.append(sublist)

    # Filtering out sublists with length greater than 1
    neue_liste = [sub for sub in temp_liste if len(sub) > 1]

    print("Sorted List:", liste)
    print("Sublists:", neue_liste)

    return liste

print(aufgabe8(startliste))