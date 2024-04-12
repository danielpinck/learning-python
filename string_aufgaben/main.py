from text_variable import text_var
from sentence_count import create_sentence_list
from find_word import find_word_output
from word_functions import *
from palindrom import palindrom


print(f"Aufgabe 1a: Mit Zahlen sind {len(create_word_list(text_var))} Worte im Text.")
print(f"Aufgabe 1b: Ohne Zahlen sind {word_count(text_var)} Worte im Text.")
print(f"Aufgabe 2:  {create_sentence_list(text_var)} Sätze im Text.")
print(f"Aufgabe 3:  {find_word_output(text_var)}")
print(f"Aufgabe 4:  {world_length(text_var)}")
print(f"Aufgabe 5: Die häufigsten 3 Wörter: ")
print(most_words(text_var))
# print(f"Aufgabe 6:  {palindrom()}")
    

