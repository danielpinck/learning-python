type_liste = [True, True, False, 1,70,9, "abc", "d","test"]
def aufgabe7(liste):
    bools = 0
    ints = 0
    strings = 0
    bool_liste = []
    int_liste = []
    string_liste = []
    true_count = 0
    longest_string = ""
    for i in liste:
        if isinstance(i, bool):
            bools += 1
            
            bool_liste.append(i)
        elif isinstance(i, int):
            ints += 1
            
            int_liste.append(i)
        elif isinstance(i, str):
            strings += 1
            
            string_liste.append(i)
    for i in bool_liste:
        
        if i == True:
            true_count += 1
    for i in string_liste:
        
        if len(i) > len(longest_string):
            longest_string = i
        
  
    print(f"{bools} Booleans")
    print(f"{ints} Integers")
    print(f"{strings} Strings")
    print(f"{true_count} True in der Liste")
    print(f"{max(int_liste)} ist der höchste Integer in der Liste")
    print(f"{longest_string} ist das längste Wort in der Liste")

aufgabe7(type_liste)