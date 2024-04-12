import string

class Chiffre:
    def __init__(self, secret_message, password):
        self.secret_message = secret_message
        self.password = password


    def list_creation(self):
        abc_lower = list(string.ascii_lowercase)
        abc_upper = list(string.ascii_uppercase)
        punct_list = list(string.punctuation)
        # space_list = list(string.whitespace)
        other_list = ["Ä", "Ö", "Ü", "ß", "ä", "ö", "ü", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
        self.all_list = abc_lower + abc_upper + punct_list + other_list
        
    def set_message(self):
        self.secret_message = input("Welcher Text soll verschlüsselt werden?\n")
        return self.secret_message
    
    def set_password(self):
        self.password = input("Mit Welchem Passwort soll der Text verschlüsselt werden?\n")
        return self.password


    def password_function(self):
        password_int = ""
        for i in self.password:
            password_int += str(self.all_list.index(i)+1)

        pass_loop = len(self.secret_message)//len(self.password)   
        password_int = password_int * pass_loop

        for i in range(len(self.secret_message)-len(password_int)):
            password_int += password_int[i+1]

        return password_int


    def cipher(self, num, cipher_string=""):
        self.cipher_string = cipher_string
        for i in self.secret_message:
            if num + self.all_list.index(i) < len(self.all_list):
                self.cipher_string += self.all_list[(self.all_list.index(i)+num)]                
            elif num + self.all_list.index(i) >= len(self.all_list):
                self.cipher_string += self.all_list[(self.all_list.index(i)+num)-len(self.all_list)]

        return self.cipher_string

    def decipher(self, num, decipher_string=""):
        self.decipher_string = decipher_string
        for i in self.cipher_string:
            if self.all_list.index(i) - num >= 0:
                    self.decipher_string += self.all_list[(self.all_list.index(i)-num)]
            elif self.all_list.index(i) - num < 0:
                    self.decipher_string += self.all_list[self.all_list.index(i) - num]
        
        return self.decipher_string
    
    def cipher_loop(self):
        
        for i in self.password_function():
            result_cipher = self.cipher(int(i))
        
        print(result_cipher)

        for i in self.password_function():
            result_decipher = (self.decipher(int(i)))

        print(result_decipher)

def main():
    chiffre = Chiffre("", "")
    chiffre.list_creation()
    chiffre.set_message()
    chiffre.set_password()
    chiffre.password_function()
    chiffre.cipher_loop()


main()


# pass_input = password_function(all_list, input("Input the cipher number: "))





# self.secret_message = "hey wie gehts"

# abc_lower = list(string.ascii_lowercase)
# abc_upper = list(string.ascii_uppercase)
# punct_list = list(string.punctuation)
# # space_list = list(string.whitespace)
# other_list = ["Ä", "Ö", "Ü", "ß", "ä", "ö", "ü", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
# all_list = abc_lower + abc_upper + punct_list + other_list
# password = "AYAYA"

# def password_function(liste, password):
#     password_int = ""

#     for i in password:
#         password_int += str(liste.index(i)+1)

#     pass_loop = len(self.secret_message)//len(password)
    
#     password_int = password_int * pass_loop

#     for i in range(len(self.secret_message)-len(password_int)):
#         password_int += password_int[i+1]

#     return password_int


# def cipher_function(liste, num):
#     cipher_string = ""
#     for i in self.secret_message:
#         if num + liste.index(i) < len(liste):
#             cipher_string += liste[(liste.index(i)+num)]                
#         elif num + liste.index(i) >= len(liste):
#             cipher_string += liste[(liste.index(i)+num)-len(liste)]

#     return cipher_string

# def decipher(cipher_string, liste, num):
    
#     decipher_string = ""
#     for i in cipher_string:
#         if liste.index(i) - num >= 0:
#                 decipher_string += liste[(liste.index(i)-num)]
#         elif liste.index(i) - num < 0:
#                 decipher_string += liste[liste.index(i) - num]
#     return decipher_string


# print(self.secret_message)

# for i in (password_function(all_list, password)):
#     result_cipher = cipher_function(all_list, int(i))

# print(result_cipher)

# # pass_input = password_function(all_list, input("Input the cipher number: "))

# for i in (password_function(all_list, password)):
#     result_decipher = (decipher(result_cipher, all_list, int(i)))

# print(result_decipher)
