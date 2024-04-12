import random

random_liste = []
def aufgabe1(elemente):
    random.seed()
    for i in range(elemente):
        random_liste.append(random.randint(1,10))
    return random_liste



def aufgabe2(liste):
    mittelwert = 0
    for i in range(len(random_liste)):
        mittelwert += random_liste[i]
    mittelwert = mittelwert/len(random_liste)
    return mittelwert


def aufgabe3(liste):
    neue_liste = []
    
    for i in range(len(liste)):
        summe = 0
        for j in str(liste[i]):
            summe += int(j)
        neue_liste.append(summe)
    return neue_liste

def aufgabe4(elemente):

    for i in range(elemente):
        random_liste.append(random.randint(1,20))
    return random_liste

def list_sort(liste):
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
    return "Jede Zahl kommt nur einmal vor" if highest == 1 else f"{count} kommt {highest} vor und ergibt {highest * count}"

def aufgabe5(zahl):
    star_list = []
    for i in range(zahl):
        star_list.append("*")
        star_string = " ".join(star_list)
        print(star_string.center(zahl*2, " "))




        


