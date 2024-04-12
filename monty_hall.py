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
        player_choice = input("Choose door 1, 2 or 3\nInput: ")
        if player_choice == "1":
            player_choice = 1

            check_valid_input = False
        elif player_choice == "2":
            player_choice = 2

            check_valid_input = False
        elif player_choice == "3":
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


def change_door(player_choice, host_choice):
    change_door_input = input(f"Do you want to change your choice of door y/n?\nInput: ")
    if change_door_input == "y":
            player_choice = 6 - player_choice - host_choice
            
            print(f"You changed your choice to {player_choice}")
    elif change_door_input == "n":
        print("You didn't change your choice")
    else:
        print("Invalid Input. Try again.")

    return player_choice

def check_if_winner(player_choice):
    if doors_list[player_choice-1] == 1:
        win_state = True
    else:
        win_state = False
    return print("You won!") if win_state == True else print("You lost!")




door1, door2, door3, doors_list = setup_list()
print(doors_list)

player_choice = choose_door()
print(f"Player chooses door {player_choice}")

host_choice, host_value = host(door1, door2, door3, player_choice)
print(f"The host opens door {host_choice} with value {host_value}")

player_choice = change_door(player_choice, host_choice)
print(f"Player chooses door {player_choice}")

check_if_winner(player_choice)






    
        