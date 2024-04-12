import keyboard, os, random

class Game:
    def __init__(self):
        self.player_symbol = "@"
        self.door = "D"
        self.item_list = ["$", "K"]
        self.item_counter = [0,0]
        self.room = []

    def create_matrix(self):
        width_length = random.randint(16,20)
        for i in range(random.randint(9,12)):
            width_list = [" "] * width_length
            self.room.append(width_list)



    def build_walls(self):
        
        for i in range(len(self.room[0])):
            self.room[0][i] = "#"
            self.room[-1][i] = "#"
        for j in range(len(self.room)):
            self.room[j][0] = "#"
            self.room[j][-1] = "#"

    def spawn_player(self):
        x = len(self.room)
        y = len(self.room[0])
        self.player_x = random.randrange(1, x-1)
        self.player_y = random.randrange(1, y-1)
        self.room[self.player_x][self.player_y] = self.player_symbol

    def spawn_door(self):
        x = len(self.room)
        y = len(self.room[0])
        self.door_x = random.randrange(1, x-1)
        self.door_y = random.randrange(1, y-1)
        while self.room[self.door_x][self.door_y] != " ":
            self.door_x = random.randrange(1, x-1)
            self.door_y = random.randrange(1, y-1)
        else:
            self.room[self.door_x][self.door_y] = self.door

    def spawn_objects(self):
        x = len(self.room)
        y = len(self.room[0])
        self.object_row = random.randrange(1, x-1)
        self.object_column = random.randrange(1, y-1)
        for i in range(3):
            while self.room[self.object_row][self.object_column] != " ":
                self.object_row = random.randrange(1, x-1)
                self.object_column = random.randrange(1, y-1)
            else:
                self.room[self.object_row][self.object_column] = self.item_list[0]
        while self.room[self.object_row][self.object_column] != " ":
                self.object_row = random.randrange(1, x-1)
                self.object_column = random.randrange(1, y-1)
        else:
            self.room[self.object_row][self.object_column] = self.item_list[1]
    
    # def detect_objects(self):
    #     self.item_counter[self.item_list.index(self.go_right)] += 1
    #     self.item_counter[self.item_list.index(self.go_left)] += 1


    def move_player(self, direction):
        self.go_right = self.room[self.player_x][self.player_y + 1]
        self.go_left = self.room[self.player_x][self.player_y - 1]
        self.go_down = self.room[self.player_x+1][self.player_y]
        self.go_up = self.room[self.player_x-1][self.player_y]

        if direction == "nach-rechts" and self.go_right != "#":
            if self.go_right == " ":                
                self.room[self.player_x][self.player_y], self.room[self.player_x][self.player_y + 1] = \
                    self.room[self.player_x][self.player_y + 1], self.room[self.player_x][self.player_y]
                self.player_y += 1
            elif self.go_right in self.item_list:
                self.item_counter[self.item_list.index(self.go_right)] += 1
                self.room[self.player_x][self.player_y], self.room[self.player_x][self.player_y + 1] = \
                    " ", self.room[self.player_x][self.player_y]
                self.player_y += 1
                                        
        elif direction == "nach-links" and self.go_left != "#":
            if self.go_left == " ":                
                self.room[self.player_x][self.player_y], self.room[self.player_x][self.player_y - 1] = \
                    self.room[self.player_x][self.player_y - 1], self.room[self.player_x][self.player_y]
                self.player_y -= 1
            elif self.go_left in self.item_list:
                self.item_counter[self.item_list.index(self.go_left)] += 1
                self.room[self.player_x][self.player_y], self.room[self.player_x][self.player_y - 1] = \
                    " ", self.room[self.player_x][self.player_y]
                self.player_y -= 1
        elif direction == "nach-unten" and self.go_down != "#":
            if self.go_down == " ":                
                self.room[self.player_x][self.player_y], self.room[self.player_x+1][self.player_y] = \
                    self.room[self.player_x+1][self.player_y], self.room[self.player_x][self.player_y]
                self.player_x += 1
            elif self.go_down in self.item_list:
                self.item_counter[self.item_list.index(self.go_down)] += 1
                self.room[self.player_x][self.player_y], self.room[self.player_x + 1][self.player_y] = \
                    " ", self.room[self.player_x][self.player_y]
                self.player_x += 1
        elif direction == "nach-oben" and self.go_up != "#":
            if self.go_up == " ":                
                    self.room[self.player_x][self.player_y], self.room[self.player_x-1][self.player_y] = \
                        self.room[self.player_x-1][self.player_y], self.room[self.player_x][self.player_y]
                    self.player_x -= 1
            elif self.go_up in self.item_list:
                self.item_counter[self.item_list.index(self.go_up)] += 1
                self.room[self.player_x][self.player_y], self.room[self.player_x - 1][self.player_y] = \
                    " ", self.room[self.player_x][self.player_y]
                self.player_x -= 1
             
        # if direction == "nach-rechts" and self.room[self.player_x][self.player_y + 1] != "#":
        #         self.room[self.player_x][self.player_y], self.room[self.player_x][self.player_y + 1] = \
        #             self.room[self.player_x][self.player_y + 1], self.room[self.player_x][self.player_y]
        #         self.player_y += 1
        # elif direction == "nach-links" and self.room[self.player_x][self.player_y - 1] != "#":
        #         self.room[self.player_x][self.player_y], self.room[self.player_x][self.player_y - 1] = \
        #             self.room[self.player_x][self.player_y - 1], self.room[self.player_x][self.player_y]
        #         self.player_y -= 1
        # elif direction == "nach-unten" and self.room[self.player_x+1][self.player_y] != "#":
        #         self.room[self.player_x][self.player_y] = " "
        #         self.player_x += 1
        #         self.room[self.player_x][self.player_y] = self.player_symbol
        # elif direction == "nach-oben" and self.room[self.player_x-1][self.player_y] != "#":
        #         self.room[self.player_x][self.player_y] = " "
        #         self.player_x -= 1
        #         self.room[self.player_x][self.player_y] = self.player_symbol


    def print_room(self):
        os.system('cls')
        print(f"row {self.player_x} column {self.player_y} {self.item_list[0]}: {self.item_counter[0]} Key: {self.item_counter[1]}")
        for row in self.room:
            print(*row)
        if self.item_counter[1] == 1:
            print("You found a key!")

def on_key_press(event, game):
    if event.name in ["nach-rechts", "nach-links", "nach-unten", "nach-oben"]:
        game.move_player(event.name)
        game.print_room()

def main():
    game = Game()
    game.create_matrix()
    game.build_walls()
    game.spawn_player()
    game.spawn_objects()
    game.spawn_door()
    game.print_room()

    keyboard.on_press(lambda event: on_key_press(event, game))

    keyboard.wait("esc")

if __name__ == "__main__":
    main()

