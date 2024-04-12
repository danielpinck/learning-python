
import string
abc_string = "zebra"

abc_lower = list(string.ascii_lowercase)
abc_upper = list(string.ascii_uppercase)
punct_list = list(string.punctuation)
space_list = list(string.whitespace)
umlaut_liste = ["Ä", "Ö", "Ü", "ß", "ä", "ö", "ü"]
all_list = abc_lower + abc_upper + punct_list + space_list + umlaut_liste


def cipher_function(liste, num):
    
    cipher_string = ""
    for i in abc_string:
        if num + liste.index(i) < len(liste):
            cipher_string += liste[(liste.index(i)+num)]                
        elif num + liste.index(i) >= len(liste):
            cipher_string += liste[(liste.index(i)+num)-len(liste)]

    return cipher_string



def decipher(cipher_string, liste, num):
    # num = int(input("Input the cipher number: "))
    decipher_string = ""
    for i in cipher_string:
        if i in liste:
            if liste.index(i) - num >= 0:
                decipher_string += liste[(liste.index(i)-num)]
            elif liste.index(i) - num < 0:
                decipher_string += liste[liste.index(i) - num]
    return decipher_string

def code_cracker(liste):
    num = 1
    for i in range(len(liste)):
        print(decipher(cipher_function(all_list, 3), all_list,num))
        num += 1



# print(abc_string)
print(cipher_function(all_list, 3))
print(decipher(cipher_function(all_list, 3), all_list,3))
# code_cracker(all_list)
