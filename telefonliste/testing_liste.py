import csv

def new_contact():

    with open("contacts.csv", "r") as file:
        contacts_num = 0
        for line in file:
            contacts_num += 1
    with open("contacts.csv", "a", newline="") as file:
        vorname = input("Vorname eingeben: ")
        nachname = input("Nachname eingeben: ")
        raumnummer = input("Raumnummer eingeben: ")
        telefonnummer = input("Telefonnummer eingeben: ")

        csv_writer = csv.writer(file)
        csv_writer.writerow([contacts_num, vorname, nachname, raumnummer, telefonnummer])

def create_list():
    with open("contacts.csv", "r") as file:
                csv_reader = csv.reader(file)
                csv_list = list(csv_reader)
    return csv_list
def show_contact(csv_list):
    
    for i in range(len(csv_list)):
            print(*csv_list[i])
    return csv_list

def bubble_num(liste, index):

    
    for j in range(len(liste)-1):
        for i in range(1,len(liste)-1 - j):
            if liste[i][index] > liste[i+1][index]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste

def main():
     while True:
        menu_input = input("n for new, s for show, q for quit, v for sort by vorname: ")
        if menu_input == "n":
            new_contact()
        if menu_input == "s":
            liste = create_list()
            show_contact(liste)
        if menu_input == "v":
             list_to_sort = create_list()
             bubble_num(list_to_sort, 1)
             max_length = max(len(item) for item in list_to_sort)
             for i in range(len(list_to_sort)):
                     
                     print(*f"{str(list_to_sort[i]):<{max_length}}")
             
        if menu_input == "u":
             list_to_sort = show_contact()
             print(list_to_sort)
        
             
        if menu_input == "q":
            break

main()

