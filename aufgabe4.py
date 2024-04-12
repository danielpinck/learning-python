# AUFGABE 4
print()
print("AUFGABE 4")


def ist_prim(zahl):
    y = 0
    if zahl <= 2000 and zahl > 0:
        for i in range(1, zahl):
            if zahl % i == 0:
                y += 1
        if y == 1:
            return True
        else:
            return False
    else:
        return None
    

print(ist_prim(-5))  
print(ist_prim(8))  
print(ist_prim(23))  
print(ist_prim(1))  