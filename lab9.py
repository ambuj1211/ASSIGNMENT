def GCD(a, b):
    if(b == 0):
        return a
    else:
        return GCD(b, a % b)

print("GCD = ",GCD(int(input("Give an integer: ")),int(input("Give another integer: "))))

''' 
OUTPUT

Give an integer: 8
Give another integer: 12
GCD =  4

'''