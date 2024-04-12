import time
before = time.time_ns()

num_list = [23,13,8,17,7,26,856,874,369,312,547,12,365,412,32,65,11,21,32,51]
print(f"Original list: {num_list}")
# def bubble_num(liste):
#     for j in range(len(liste)-1):

#         for i in range(len(liste)-1 - j):
#             if liste[i] > liste[i+1]:
#                 liste[i], liste[i+1] = liste[i+1], liste[i]


# bubble_num(num_list)
# print(f"Sorted list: {num_list}")

# name_list = ["Meier", "Lindner ", "Jensen", "Kohl", "Marz", "Hansen ", "Lass"]
# print(name_list)
# def buuble_name_len(liste):
#     for i in range(len(liste)-1):
#         for j in range(len(liste)-1):
#             if len(liste[j]) > len(liste[j+1]):
#                 liste[j], liste[j+1] = liste[j+1], liste[j]

                
#             if len(liste[j]) == len(liste[j+1]):
#                 if liste[j][0] > liste[j+1][0]:
#                     liste[j], liste[j+1] = liste[j+1], liste[j]
# buuble_name_len(name_list)
# print(name_list)

def bubble_while(liste):

    tausch = True
    while tausch:
        tausch = False
        i = 0
        while i < len(liste)-1:

            
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                
                tausch = True
            i += 1
    
bubble_while(num_list)
print(num_list)
after = time.time_ns()
print((after-before)/1000000)
