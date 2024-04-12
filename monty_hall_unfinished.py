import random
def setup():
    doors_list = [1,2,3]
    random.shuffle(doors_list)
    winner = random.randint(1,3)
    player_choice = random.randint(1,3)

    return doors_list, winner, player_choice

def host(doors_list, winner, player_choice):

    if winner == player_choice:
        doors_list.remove(winner)
        host_door = doors_list[random.choice([0,1])]
   

    else:
        doors_list.remove(winner)
        doors_list.remove(player_choice)
        host_door =  doors_list[0]
    return host_door
    
#def player_decision(host_door)

print(setup())
print(host(*setup()))



new_choice = 0


    
        