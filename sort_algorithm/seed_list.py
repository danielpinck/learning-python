import random
random_list = []

def new_seed_func():
    new_seed = random.randint(1,5000)
    return new_seed

def fill_list(elements, liste, num_range, random_seed = 1337):
    random_seed = new_seed_func()
    random.seed(random_seed)
    liste = []
    for i in range(elements):
        liste.append(random.randint(1,num_range))
    return elements, liste, num_range, random_seed



elements, liste, num_range, random_seed = fill_list(10, random_list, 100)
print(elements)
print(liste)
print(num_range)
print(random_seed)


# import random
# random_list = []

# def fill_list(elements, liste, num_range, random_seed=1337):
#     if random_seed is not 1337:
#         random.seed(random_seed)
#     liste = []
#     for i in range(elements):
#         liste.append(random.randint(1,num_range))
#     return elements, liste, num_range, random_seed

# elements, liste, num_range, random_seed = fill_list(10, random_list, 100)
# print(elements)
# print(liste)
# print(num_range)
# print(random_seed)

# elements, liste, num_range, random_seed = fill_list(10, random_list, random.randint(1,4000))
# print(random_seed)


