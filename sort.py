liste = [10,12,8,8,7,1,5,23,187,24,2,689]
liste_abc = ["p","b","o","p","l","e","t","k"]


def list_sort(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
                if liste[i] < liste[j]:
                    temp = liste[j]
                    liste[j] = liste[i]
                    liste[i] = temp
    return liste

print(list_sort(liste))
print(list_sort(liste_abc))
