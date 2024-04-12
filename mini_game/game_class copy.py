import keyboard, os, random

class Game:
    def __init__(self):
        self.player_symbol = "@"
        self.questionmark = "?"
        self.test_room = []

        # self.player_x = 0
        # self.player_y = 0
        # self.object_row = 0
        # self.object_column = 0


    def create_matrix(self):
        width_length = random.randint(16,20)
        for i in range(random.randint(9,12)):
            width_list = [" "] * width_length
            self.test_room.append(width_list)



    def build_walls(self):
        
        for i in range(len(self.test_room[0])):
            self.test_room[0][i] = "#"
            self.test_room[-1][i] = "#"
        for j in range(len(self.test_room)):
            self.test_room[j][0] = "#"
            self.test_room[j][-1] = "#"

    def spawn_object(self):
        x = len(self.test_room)
        y = len(self.test_room[0])
        self.player_x = random.randrange(1, x-1)
        self.player_y = random.randrange(1, y-1)
        self.test_room[self.player_x][self.player_y] = self.player_symbol

    def spawn_questionmark(self):
        x = len(self.test_room)
        y = len(self.test_room[0])
        self.object_row = random.randrange(1, x-1)
        self.object_column = random.randrange(1, y-1)
        while self.test_room[self.object_row][self.object_column] != " ":
            self.object_row = random.randrange(1, x-1)
            self.object_column = random.randrange(1, y-1)
        else:
            self.test_room[self.object_row][self.object_column] = self.questionmark
    
    
    # def check_for_items(self):
    #      if self.test_room[self.player_x][self.index_x + 1]   


    def move_player(self, direction):
        # index_x = self.test_room[self.player_x].index(self.player_symbol)
        player_position = self.test_room[self.player_x][self.player_y]
        player_x_change = 0
        player_y_change = 0

        if direction == "nach-rechts" and self.test_room[self.player_x][self.player_y + 1] != "#":
                self.test_room[self.player_x][self.player_y], self.test_room[self.player_x][self.player_y + 1] = \
                    self.test_room[self.player_x][self.player_y + 1], self.test_room[self.player_x][self.player_y]
                self.player_y += 1
        elif direction == "nach-links" and self.test_room[self.player_x][self.player_y - 1] != "#":
                self.test_room[self.player_x][self.player_y], self.test_room[self.player_x][self.player_y - 1] = \
                    self.test_room[self.player_x][self.player_y - 1], self.test_room[self.player_x][self.player_y]
                self.player_y -= 1
        elif direction == "nach-unten" and self.test_room[self.player_x+1][self.player_y] != "#":
                self.test_room[self.player_x][self.player_y] = " "
                self.player_x += 1
                self.test_room[self.player_x][self.player_y] = self.player_symbol
        elif direction == "nach-oben" and self.test_room[self.player_x-1][self.player_y] != "#":
                self.test_room[self.player_x][self.player_y] = " "
                self.player_x -= 1
                self.test_room[self.player_x][self.player_y] = self.player_symbol

        
        
        # if direction == "nach-rechts" and self.player_y and self.test_room[self.player_x][self.player_y + 1] != "#":
        #         self.test_room[self.player_x][self.player_y], self.test_room[self.player_x][self.player_y + 1] = \
        #             self.test_room[self.player_x][self.player_y + 1], self.test_room[self.player_x][self.player_y]
        #         self.player_y += 1
        # elif direction == "nach-links" and self.test_room[self.player_x][self.player_y - 1] != "#":
        #         self.test_room[self.player_x][self.player_y], self.test_room[self.player_x][self.player_y - 1] = \
        #             self.test_room[self.player_x][self.player_y - 1], self.test_room[self.player_x][self.player_y]
        #         self.player_y -= 1
        # elif direction == "nach-unten" and self.test_room[self.player_x+1][self.player_y] != "#":
        #         self.test_room[self.player_x][self.player_y] = " "
        #         self.player_x += 1
        #         self.test_room[self.player_x][self.player_y] = self.player_symbol
        # elif direction == "nach-oben" and self.test_room[self.player_x-1][self.player_y] != "#":
        #         self.test_room[self.player_x][self.player_y] = " "
        #         self.player_x -= 1
        #         self.test_room[self.player_x][self.player_y] = self.player_symbol



    def print_room(self):
        os.system('cls')
        print(f"row {self.player_x} column {self.player_y}")
        for row in self.test_room:
            print(*row)

def on_key_press(event, game):
    if event.name in ["nach-rechts", "nach-links", "nach-unten", "nach-oben"]:
        game.move_player(event.name)
        game.print_room()

def main():
    game = Game()
    game.create_matrix()
    game.build_walls()
    game.spawn_object()
    game.spawn_questionmark()
    game.print_room()

    keyboard.on_press(lambda event: on_key_press(event, game))

    keyboard.wait("esc")

if __name__ == "__main__":
    main()
