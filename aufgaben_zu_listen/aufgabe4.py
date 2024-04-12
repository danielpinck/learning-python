liste_temp = ["a", "a", "a", "b"]
def aufgabe4(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
                if liste[i] < liste[j]:
                    temp = liste[j]
                    liste[j] = liste[i]
                    liste[i] = temp
    temp_liste = []
    for i in range(len(liste)): 
        temp_liste.append(0)

    for i in range(len(liste)):
        for j in range(len(liste)):
                if liste[i] == liste[j]:
                    temp_liste[i] += 1


    highest = 0
    count = 0
    for l in range(len(temp_liste)):
        
        if temp_liste[l] >= highest:
             
            highest = temp_liste[l]
            count = liste[l]
    print(liste)
    arrow_list = []
    arrow_list = liste
    for i in range(len(arrow_list)):
        if arrow_list[i] != count:
              arrow_list[i] = " "*len(str(arrow_list[i]))
        elif arrow_list[i] == count:
             arrow_list[i] = "^"*len(str(arrow_list[i]))
    arrow_string = f" {'  '.join(arrow_list)} "
    print(arrow_string)
    return "Every number is unique" if highest == 1 else f"{count} is the highest and appears {highest} times.\n{count} * {highest} = {highest * count}"



print(aufgabe4(liste_temp))