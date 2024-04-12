
from string_aufgaben.word_functions import *
from text_variable import text_var
def word_length(text, text_var):
    remove_hyphen(text_var)
    text_list = create_word_list(text)
    longest_word_len = 0

    for i in text_list:
        if "," in i:
            i = i.replace(",", "")
        if len(i) > longest_word_len:
            longest_word = i
            longest_word_len = len(i)

    return longest_word_len, longest_word

def word_length_output(text, text_var):

    longest_word_len, longest_word = word_length(text, text_var)
    return f"{longest_word} is mit {longest_word_len} Buchstaben das längste Wort"

print(word_length_output())



    
