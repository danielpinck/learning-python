def prime(num):
    isprime = 0
    if num == 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
    
    

print(prime(111113111))
