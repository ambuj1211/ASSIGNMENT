n = int(input("Give an integer: "))
m = n*2-1
for i in range(n):
    j = i
    for k in range(m):
        if k <= int(m/2):
            if k < (int(m/2)-(j)):
                print("",end=" ")
            else:
                j = j+1
                print(j,end="")
        else:
            j = j-1
            if j>i:
                print(j,end="")
            else:
                break
    print()
