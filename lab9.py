def GCD(a, b):
    if(b == 0):
        return a
    else:
        return GCD(b, a % b)

def help(a,b):
    if(a>b):
        return GCD(a,b)
    else:
        return GCD(b,a)

print("GCD = ",help(int(input("Give an integer: ")),int(input("Give another integer: "))))