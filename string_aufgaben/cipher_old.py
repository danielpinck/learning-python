import string

abc_string = "hey wie gehts123"


# space_list = list(string.whitespace)
other_list = ["Ä", "Ö", "Ü", "ß", "ä", "ö", "ü", " "]
all_list = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.punctuation) + list(string.digits) + other_list

password = "bbb"

def password_function(liste, password):
    password_int = ""

    for i in password:
        password_int += str(liste.index(i)+1)

    pass_loop = len(abc_string)//len(password)
    
    password_int = password_int * pass_loop

    for i in range(len(abc_string)-len(password_int)):
        password_int += password_int[i+1]

    return password_int


def cipher_function(liste, num):
    cipher_string = ""
    for i in abc_string:
        if num + liste.index(i) < len(liste):
            cipher_string += liste[(liste.index(i)+num)]                
        elif num + liste.index(i) >= len(liste):
            cipher_string += liste[(liste.index(i)+num)-len(liste)]

    return cipher_string

def decipher(cipher_string, liste, num):
    
    decipher_string = ""
    for i in cipher_string:
        if liste.index(i) - num >= 0:
                decipher_string += liste[(liste.index(i)-num)]
        elif liste.index(i) - num < 0:
                decipher_string += liste[liste.index(i) - num]
    return decipher_string


print(abc_string)

for i in (password_function(all_list, password)):
    result_cipher = cipher_function(all_list, int(i))

print(result_cipher)

# pass_input = password_function(all_list, input("Input the cipher number: "))

for i in (password_function(all_list, password)):
    result_decipher = (decipher(result_cipher, all_list, int(i)))

print(result_decipher)
