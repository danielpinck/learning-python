from datetime import datetime
# from seed_list import fill_list
from sort_functions import *
import keyboard, os



sort_menu = [["[\033[1;5mX\033[0m]", " Bubble Sort".ljust(20, " "), ""],
             ["[ ]", " Bubble Sort While".ljust(20, " "), ""],
             ["[ ]", " Insertion Sort".ljust(20, " "), ""],
             ["[ ]", " Selection Sort".ljust(20, " "), ""],
             ["[ ]", " Shell Sort".ljust(20, " "), ""],
             ["[ ]", f" New Seed ()".ljust(20, " "), ""]]

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
    if event.name == "enter":
        run_sort()
num_list = []
liste, random_seed = fill_list(20, num_list, 100, 100) 
def run_sort():
    global liste, random_seed
    elements = 15000
    num_range = 100
    


    # random_seed = 1337
   
    print(f"List creation: {time_function(fill_list, elements, liste, num_range, random_seed)}")

    if sort_menu[0][2] != "":
        num_list = []
        time_function(fill_list, elements, num_list, num_range, random_seed)
        print("Bubble Sort:".ljust(20," ") + f"{time_function(bubble_num, num_list)}")

    if sort_menu[1][2] != "": 
        num_list = []
        time_function(fill_list, elements, num_list, num_range, random_seed)
        print("Bubble Sort While:".ljust(20," ") + f"{time_function(bubble_while, num_list)}")
        # print(num_list)
    if sort_menu[2][2] != "": 
        num_list = []
        time_function(fill_list, elements, num_list, num_range, random_seed)
        print(f"Insertion Sort:".ljust(20," ") + f"{time_function(insertion_sort, num_list)}")

    if sort_menu[3][2] != "": 
        num_list = []
        time_function(fill_list, elements, num_list, num_range, random_seed)
        print(f"Selection Sort:".ljust(20," ") + f"{time_function(selection_sort, num_list)}")
        # print(num_list)
    if sort_menu[4][2] != "": 
        num_list = []
        time_function(fill_list, elements, num_list, num_range, random_seed)
        print(f"Shell Sort:".ljust(20," ") + f"{time_function(shell_sort, num_list)}")
        print(random_seed)
    if sort_menu[0][2] == "" and sort_menu[1][2] == "" and sort_menu[2][2] == "" and sort_menu[3][2] == "" and sort_menu[4][2] == "" and sort_menu[5][2] != "": 
        num_list = []
        random_seed = random.randint(1,5000)
        
        print(random_seed)


os.system('cls') 
for i in range(len(sort_menu)):
    print(*sort_menu[i])



keyboard.on_press(menu)
keyboard.wait("esc")


