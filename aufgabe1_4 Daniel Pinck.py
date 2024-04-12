# AUFGABE 1
def berechne_arbeitslohn(arbeitsstunden):
    stundenlohn = 15.5
    ueberstundenlohn = 19.0
    gesamt = 0
    if arbeitsstunden <= 40:
        gesamt = arbeitsstunden * stundenlohn
    elif arbeitsstunden > 40 and arbeitsstunden <= 60:
        gesamt = 40 * stundenlohn
        ueberstunden = (arbeitsstunden - 40) * ueberstundenlohn
        gesamt += ueberstunden
    elif arbeitsstunden > 60:
        gesamt = (40 * stundenlohn) + (20 * ueberstundenlohn)
    return gesamt


print()
print("AUFGABE 1")
print(f"Der Lohn beträgt diesen Monat {berechne_arbeitslohn(60)} €")


# AUFGABE 2
'''def bmi():

    height = float(input("Gebe deine Größe in cm ein: "))
    mass = 60
    while mass <= 150:
        bmi_calculation = mass / ((height / 100)*2)
        print(f"Bei {mass} kg ist dein BMI {round(bmi_calculation, 1)}")
        mass += 10

print("AUFGABE 1")
bmi()'''
print()


# AUFGABE 3
def faculty(zahl):
    gesamt = 1
    if zahl == 0 or zahl == 1:
        gesamt = 1

    else:
        for i in range(1, zahl):
            i += 1
            gesamt *= i
    return gesamt


print()
print("AUFGABE 3")
print(faculty(7))


# AUFGABE 4
print()
print("AUFGABE 4")


def ist_prim(zahl):
    y = 0
    if zahl <= 2000 and zahl > 0:
        for i in range(1, zahl):
            if zahl % i == 0:
                y += 1
        if y == 1:
            return True
        else:
            return False
    else:
        return None
    

print(ist_prim(-5))  
print(ist_prim(775))  
print(ist_prim(23))  
print(ist_prim(1))  
