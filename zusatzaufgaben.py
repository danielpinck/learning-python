# AUFGABE Z1
liste_aufgabe1 = [1,2,3,4,5,6,7,8,9]
def liste_addieren(liste):
    
    j = 0
    for i in range(len(liste_aufgabe1)):
        if liste_aufgabe1[i]%2 == 1:
            j += liste_aufgabe1[i]
    return j
print("AUFGABE 1")
print(liste_addieren(liste_aufgabe1))

# AUFGABE Z2

def schach2(groesse):
    liste_schach2 = ""
    break_string = "\n"
    for i in range(0, int(groesse/2)):
        for i in range(0, int(groesse/2)):
            liste_schach2 += "\u2b1c\u2b1b"
        liste_schach2 += break_string
        for i in range(0, int(groesse/2)):
            liste_schach2 += "\u2b1b\u2b1c"
        liste_schach2 += break_string
    return liste_schach2

print("\nAUFGABE 2")
print(schach2(20))

# AUFGABE Z3

string_var = "teststring"
new_string = ""
for i in range(len(string_var)-1, -1, -1):
    new_string += string_var[i]
print(new_string)



# AUFGABE Z5