import random

def setup_list():
    doors_list = [0, 0, 1]
    random.shuffle(doors_list)
    return doors_list

def choose_door():
    return random.randint(1, 3)

def host(doors_list, player_choice):
    for i in range(1, 4):
        if doors_list[i-1] == 0 and i != player_choice:
            return i

def change_door(player_choice, host_choice):
    return 3

def simulate_game(num_runs):
    wins = 0
    for _ in range(num_runs):
        doors_list = setup_list()
        player_choice = choose_door()
        host_choice = host(doors_list, player_choice)
        player_choice = change_door(player_choice, host_choice)
        if doors_list[player_choice-1] == 1:
            wins += 1
    return wins / num_runs

num_runs = 100000
win_probability = simulate_game(num_runs)
print(f"Win probability after {num_runs} simulations: {win_probability}")