import keyboard, os

i = 0


player_symbol = "@"
test_room = [[player_symbol, " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],

            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "]]

def movement(event, matrix=test_room, char=player_symbol):

    global i 

    
    if event.name == "nach-rechts":
        index_x = matrix[i].index(char)
        if index_x < len(matrix[0])-1:
            matrix[i][index_x] = matrix[i][index_x + 1]
            matrix[i][index_x + 1] = char
    elif event.name == "nach-links":
        index_x = matrix[i].index(char)
        if index_x > 0:
            matrix[i][index_x] = matrix[i][index_x + -1]
            matrix[i][index_x - 1] = char
    elif event.name == "nach-unten":
        index_x = matrix[i].index(char)
        if index_x >= 0 and i < len(matrix)-1:
            matrix[i][index_x] = matrix[i+1][index_x]

            i += 1
            matrix[i][index_x] = char
    elif event.name == "nach-oben":
        index_x = matrix[i].index(char)
        if index_x >= 0 and i > 0:
            matrix[i][index_x] = matrix[i-1][index_x]
            i -= 1
            matrix[i][index_x] = char

    os.system('cls') 
    for j in range(len(matrix)):
        print(*matrix[j])


keyboard.on_press(movement)
keyboard.wait("esc")

# def schach():
#     abc_list = ["A", " B", " C", " D", " E", " F", " G", " H"]
#     row_num = 1
#     odd_row_list = ["\u2b1c","\u2b1b","\u2b1c","\u2b1b","\u2b1c","\u2b1b","\u2b1c","\u2b1b"]
#     even_row_list = ["\u2b1b","\u2b1c","\u2b1b","\u2b1c","\u2b1b","\u2b1c","\u2b1b","\u2b1c"]
#     chessboard = [abc_list, odd_row_list,even_row_list,odd_row_list,even_row_list,odd_row_list,even_row_list,odd_row_list,even_row_list]
#     for i in range(len(chessboard)):
#         print(*chessboard[i], sep="")

# schach()
# def schach2():
#     liste_schach2 = ""
#     break_string = "\n"
#     for i in range(0, 10):
#         for i in range(0, 10):
#             liste_schach2 += "\u2b1c\u2b1b"
#         liste_schach2 += break_string
#         for i in range(0, 10):
#             liste_schach2 += "\u2b1b\u2b1c"
#         liste_schach2 += break_string
#     return liste_schach2

# print(schach2())



# liste = [[char, "_", "_", "_", "_", "_", "_", "_", "_"],
#          ["_", "_", "_", "_", "_", "_", "_", "_", "_"]]