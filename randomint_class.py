import random
class RandomInteger():
    def random_integer(self):
        random_int = random.randint(1,6)
        return random_int
    
class GeneratorInput():
    def __init__(self, iteration_input):
        self.iteration_input = iteration_input

    def user_input(self):
        random_integer_object = RandomInteger()
        i = 1
        self.iteration_input = int(input("How many random numbers do you want? "))
        while i <= self.iteration_input:
            print(random_integer_object.random_integer())
            i += 1



generator_input_object = GeneratorInput(1)
generator_input_object.user_input()





