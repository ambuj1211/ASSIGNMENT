def dotproduct(lst1,lst2):
    if len(lst1) == len(lst2):
        sum = 0
        for i in range(len(lst1)):
            sum = sum + lst1[i]*lst2[i]
        return sum
    else:
        return "error"
        
lst1 = [int(item) for item in input("Enter the list items : ").split()]
lst2 = [int(item) for item in input("Enter the list items : ").split()]

print("Dot product : ",dotproduct(lst1,lst2))



'''
output 

Enter the list items : 2 3 4 5 6
Enter the list items : 10 20 30 40 50
Dot product :  700

'''
