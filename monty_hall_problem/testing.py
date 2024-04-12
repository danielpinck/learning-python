import random

door_list = [0,0,0]
door_list[random.randint(0,2)] = 1
door1 = door_list[0]
door2 = door_list[1]
door3 = door_list[2]

first_choice = random.randint(0,2)
'''
def player_choose():
    
    first_choice = random.randint(0,2)
    return first_choice

def moderator_chose(player, d1, d2, d3):
    

    if door_list[0] != 1 and door_list[0] != player:

'''

print(f"3 Türen {door_list}")
print(f"Spieler wählt Tür {first_choice+1}")
print(f"Gewählte Tür hat den Wert {door_list[first_choice]}")



if door_list[first_choice] == 1:
    if door_list[0] == 1:
        print(f"1 Moderator wählt Tür {random.choice([2,3])}")
    elif door_list[1] == 1:
        print(f"1 Moderator wählt Tür {random.choice([1,3])}")
    elif door_list[2] == 1:
        print(f"1 Moderator wählt Tür {random.choice([1,2])}")
        
else:
    if door_list[0] == 1:
        print(f"Moderator wählt Tür {random.choice([2,3])}")
    elif door_list[1] == 1:
        print(f"Moderator wählt Tür {random.choice([1,3])}")
    elif door_list[2] == 1:
        print(f"Moderator wählt Tür {random.choice([1,2])}")






