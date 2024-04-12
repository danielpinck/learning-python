def palindrom():
    word = input("Überprüfe ob ein wort oder satz ein Palindrom ist \nInput:")
    word_reversed = ""
    word_check = word.replace("- ", "").replace("-", "").replace(",", "").replace(".", "").replace(":", "").replace("!", "").replace(";", "").lower()
    for i in word_check:
        word_reversed = i + word_reversed
    return f"{word_check} ist ein Palindrom" if word_check == word_reversed else f"{word_check} ist kein Palindrom"
