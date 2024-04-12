from text_variable import text_var

def remove_hyphen(text):
    text = text.replace("- ", "").replace("-", "")
    return text

def create_word_list(text):
    text = remove_hyphen(text)
    text = text.replace(",", "").replace(".", "")
    text_list = text.split(" ")
    return text_list

def remove_dupes(text_list):
    unique_words = []
    for i in text_list:
        i = i.lower()
        if i not in unique_words:
            unique_words.append(i)
    return unique_words

def clean_text(text):
    text = text.replace("- ", "").replace("-", "").replace(",", "").replace(".", "").lower()
    return text



def make_lower(text_list):
    lower_list = []
    for i in text_list:
        lower_list.append(i.lower())
    return lower_list

def word_freq(text_list, text):
    freq_list = []
    for i in text_list:
        freq = text.count(i)
        freq_list.append((i, freq))
    return freq_list

def sort_highest(a):
    return a[1]

def create_word_count_list(text):
    text = clean_text(text)
    text_list = text.split(" ")
    return text_list


def most_words():
    text_list = create_word_count_list(text_var)  
    unique_words = remove_dupes(text_list)
    lower_list = make_lower(unique_words)
    three_words = word_freq(lower_list, text_list)  
    three_words.sort(key=sort_highest)
    print(text_list)
    return f'Das Wort "{three_words[-1][0]}" kommt {three_words[-1][1]} mal vor \nDas Wort "{three_words[-2][0]}" kommt {three_words[-2][1]} mal vor \nDas Wort "{three_words[-3][0]}" kommt {three_words[-3][1]} mal vor'



print(most_words())