from aufgabe1 import aufgabe1
from aufgabe2 import aufgabe2
from aufgabe3 import aufgabe3
from aufgabe4 import aufgabe4
from elements import elements
from aufgabe5 import aufgabe5, a5input


def menu():
    menu_bool = True
    while menu_bool:
        auswahlliste = "1. Random Number Generator\n2. Calculate Average\n3. Calculate Digit Sum\n4. Most Frequently Occurring Number\n5. Triangle Generator\n0. End Programm"
        
        print(auswahlliste)
        auswahl = input("Auswahl: ")
        if auswahl == "0":
            menu_bool = False
        elif auswahl == "1":

            print(aufgabe1(*elements()))
        elif auswahl == "2":
            average, liste = aufgabe2(aufgabe1(*elements()))
            print(f"The Numbers {liste}")
            print(f"The Average {average}")
        elif auswahl == "3":
            digit_sum = aufgabe3(aufgabe1(*elements()))
            print(f"The List of Digit Sums {digit_sum}")
        elif auswahl == "4":
            highest_num = aufgabe4(aufgabe1(*elements()))
            print(highest_num)
        elif auswahl == "5":
            print(aufgabe5(*a5input()))
            
            
menu()