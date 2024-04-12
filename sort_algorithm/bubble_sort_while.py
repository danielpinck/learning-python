# import time
# before = time.time_ns()

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
    return liste