import csv

def new_contact():
    with open("contacts.csv", "r") as file:
        contacts_num = 1
        for line in file:
            contacts_num += 1

    with open("contacts.csv", "a", newline="") as file: 
        
      
        vorname = input("Vorname eingeben: ")
        nachname = input("Nachname eingeben: ")
        raumnummer = input("Raumnummer eingeben: ")
        telefonnummer = input("Telefonnummer eingeben: ")

        csv_writer = csv.writer(file)
        csv_writer.writerow([contacts_num, vorname, nachname, raumnummer, telefonnummer])
    
    with open("contacts.csv", "r") as file:
        content = file.read()
        print(content)
   
new_contact()

