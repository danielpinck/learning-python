def fibo(max):
    fibi1 = 0
    fibi2 = 1
    fibiNeu = 1
    print(fibi1)
    print(fibi2)
    while fibiNeu+fibi1 <= max:
        fibiNeu = fibi1 + fibi2
        fibi1, fibi2 = fibi2, fibiNeu
        print(fibiNeu)

fibo(15)

nummern = [1,2,3,7,10]
def summeUngerade(nummernliste):
    
    summe = 0
    for i in nummernliste:
        if i == 1:
            summe += 1
        elif  i%2 != 0:
            summe += i
    return summe

print(f"Summe: {summeUngerade(nummern)}")

def prime(zahl):
    liste = []
    i = 2
    while i <= zahl:
        if zahl%i == 0:
            liste.append(i)
            zahl = zahl / i
        else:
            i += 1


    return liste

print(prime(105))

def mittel(zahl1,zahl2,zahl3):
    liste = []
    liste.append(zahl1)
    liste.append(zahl2)
    liste.append(zahl3)
    liste.sort()
    return liste[1]

print(mittel(8,9,2))


daten = [0,1,1,1]
def function_d(daten):
    
    summe = daten[0]
    i = 1
    while i < len(daten):
        summe += daten[i]
        i += 1

    durchschnitt = summe/i 
    return durchschnitt

print(function_d(daten))