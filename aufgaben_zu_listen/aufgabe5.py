def a5input():
    num_input = int(input("How large should the triangle be?\nInput: "))
    symbol_input = input("What symbol should used (*, #, + etc)?\nInput: ")
    return num_input, symbol_input

def aufgabe5(zahl, symbol):
    star_list = []
    for i in range(zahl):
        star_list.append(symbol)
        star_string = " ".join(star_list)
        print(star_string.center(zahl*2, " "))