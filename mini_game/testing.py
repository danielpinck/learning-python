import random, keyboard
# class Numbers:
#     def __init__(self) -> None:
#         self.x = [0,1]
#         self.check = 9


#     def if_check(self):
#         if self.check == 9:
#             self.check_number()

#     def check_number(self):
#         if self.x[0] == 0:
#             print(True)
#         else:
#             print(False)


# def main():
#     numbers = Numbers()
#     numbers.if_check()

# if __name__ == "__main__":
#     main()


# class Game_object:
#     def __init__(self):
#         self.set_row()
#         self.set_column()
#         self.set_symbol()

#     def set_row(self):
#         self.row = random.randint(1,10)
    
#     def set_column(self):
#         self.column = random.randint(1,10)
    
#     def set_symbol(self):
#         item_list = ["?", "+", "$" ,"%"]
        
#         self.symbol = item_list[random.randrange(len(item_list))] 
#     def print_object(self):
#         print(f"row {self.row}, column {self.column}, symbol {self.symbol}")

# x = Game_object()

# x.print_object()

class Game:
    def __init__(self) -> None:
        pass


    def move_player(self, direction):
        if direction == "nach-rechts" and direction == "nach-unten":
            print("rechts-unten")

def on_key_press(event, game):
    if event.name in ["nach-rechts", "nach-unten"]:
        game.move_player

def main():
    game = Game()
    keyboard.on_press(lambda event: on_key_press(event, game))
    keyboard.wait("esc")

if __name__ == "__main__":
    main()



