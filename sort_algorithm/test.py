import keyboard, os, sys
random_list = [1,5,100,56,2,234]

sort_menu = [["[\033[1;5mX\033[0m]", " Bubble Sort".ljust(15, " "), ""],
             ["[ ]", " Insertion Sort".ljust(15, " "), ""],
             ["[ ]", " Selection Sort".ljust(15, " "), ""]]

start = 0

def menu(event):
    global start
    if event.name == "nach-unten" and start < len(sort_menu)-1:
        if sort_menu[start][0] == "[\033[1;5mX\033[0m]":
            sort_menu[start][0] = "[ ]"
        start += 1
        sort_menu[start][0] = "[\033[1;5mX\033[0m]"
        
    elif event.name == "nach-oben" and start > 0:
        if sort_menu[start][0] == "[\033[1;5mX\033[0m]":
            sort_menu[start][0] = "[ ]"
        start -= 1
        sort_menu[start][0] = "[\033[1;5mX\033[0m]"

    if event.name == "space":
        if sort_menu[start][2] == "":
            sort_menu[start][2] = "[\033[92m\u2713\033[0m]"
        elif sort_menu[start][2] == "[\033[92m\u2713\033[0m]":
            sort_menu[start][2] = ""

            
    os.system('cls') 
    for i in range(len(sort_menu)):
        print(*sort_menu[i])
    print(start)
    
        

os.system('cls') 
for i in range(len(sort_menu)):
    print(*sort_menu[i])
print(start)
    


keyboard.on_press(menu)

keyboard.wait("esc")






def sort_function(liste):

    liste.sort()
    return liste


# print(sort_function(random_list))



