def number(num_int):
    return num_int

def menu():
    i = True
    nummer = number(5)
    while i == True:
        
        print(nummer)
        quit = input("Press q to quit, c to change number")
        if quit == "q":
            i = False
        elif quit == "c":
            nummer = number(10)
            

menu()