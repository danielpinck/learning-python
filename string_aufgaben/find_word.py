def find_word(text, find_string):
    is_in_string = find_string in text
    return is_in_string, find_string
    
    
def find_word_output(text_var):
    found_bool, find_string = find_word(text_var, "Bäckerei")
    return f"Das Wort '{find_string}' kommt vor" if found_bool == True else f"Das Wort '{find_string}' kommt nicht vor"

