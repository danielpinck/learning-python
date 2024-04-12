import random
def setup_list():
    doors_list = [0,0,1]
    random.shuffle(doors_list)
    door1 = doors_list[0]
    door2 = doors_list[1]
    door3 = doors_list[2]
    return door1, door2, door3, doors_list

def choose_door():
    check_valid_input = True
    while check_valid_input: 
        player_choice = random.randint(1,3) #input("Choose door 1, 2 or 3\nInput: ")
        if player_choice == 1: # "1":
            player_choice = 1

            check_valid_input = False
        elif player_choice == 2: # "2":
            player_choice = 2

            check_valid_input = False
        elif player_choice == 3: #"3":
            player_choice = 3

            check_valid_input = False
        else: 
            print("Invalid input. Try again")
    return player_choice

def host(door1, door2, door3, player_choice):

    if door1 == 0 and player_choice != 1:
        host_choice = 1
        host_value = door1
    elif door2 == 0 and player_choice != 2:
        host_choice = 2
        host_value = door2
    elif door3 == 0 and player_choice != 3:
        host_choice = 3
        host_value = door3
    return host_choice, host_value


def changing_door(player_choice, host_choice):
    change_door_input = "y" # input(f"Do you want to change your choice of door y/n?\nInput: ")
    if change_door_input == "y":
            player_choice = 6 - player_choice - host_choice
            
            #print(f"You changed your choice to {player_choice}")
    elif change_door_input == "n":
        print("You didn't change your choice")
    else:
        print("Invalid Input. Try again.")

    return player_choice

def not_changing_door(player_choice, host_choice):


    return player_choice



def sim_changing_door(num_runs): 
    wins = 0
    for i in range(num_runs):
        door1, door2, door3, doors_list = setup_list()


        player_choice = choose_door()


        host_choice, host_value = host(door1, door2, door3, player_choice)


        player_choice = changing_door(player_choice, host_choice)



        if doors_list[player_choice-1] == 1: 
            wins += 1
    return (wins / num_runs)*100

num_runs = 1000

win_probability = sim_changing_door(num_runs)
print(f"Win probability while changing the door: {win_probability}%")

def sim_not_changing_door(num_runs): 
    wins = 0
    for i in range(num_runs):
        door1, door2, door3, doors_list = setup_list()


        player_choice = choose_door()


        host_choice = host(door1, door2, door3, player_choice)


        player_choice = not_changing_door(player_choice, host_choice)



        if doors_list[player_choice-1] == 1: 
            wins += 1
    return (wins / num_runs)*100

num_runs = 100000

win_probability = sim_not_changing_door(num_runs)
print(f"Win probability while not changing the door: {win_probability}%")

        