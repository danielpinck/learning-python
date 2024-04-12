import string
class Testing:
    def __init__(self, text_var, integer):
        self.text_var = text_var
        self.integer = integer



    def text_test(self):
        self.text_var = "test"

    def math_test(self):
        self.num_var = 5
        
    def output(self):
        self.text_var *= self.num_var
        print(self.text_var)
        

def main():
    test = Testing("a", 1)
    test.text_test()
    test.math_test()
    test.output()

main()

        
    # def list_creation(self):
    #     self.other_list = ["Ä", "Ö", "Ü", "ß", "ä", "ö", "ü", " "]
    #     self.all_list = list(string.ascii_lowercase) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + \
    #         list(string.punctuation) + list(string.digits) + self.other_list
    #     return self.all_list