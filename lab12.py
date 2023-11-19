n = int(input("Enter number of planets: "))
lst = [int(i) for i in input("List of distances of planet: ").split()]
k = int(input("position of Aman's favourite planet in unsorted list: "))
print(lst[k-1])

'''
output

Enter number of planets: 5
List of distances of planet: 4 5 3 1 2
position of Aman's favourite planet in unsorted list: 2
5
'''