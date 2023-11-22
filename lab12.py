def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
 
n = int(input("Enter number of planets: "))
lst = [int(i) for i in input("List of distances of planet: ").split()]
k = int(input("position of Aman's favourite planet in unsorted list: "))
tem = lst[k-1]

lst.sort()
result = binary_search(lst, tem)
print("Element is present at index: ", result+1)


'''
output of Question No. 12

Enter number of planets: 5
List of distances of planet: 4 5 3 1 2
position of Aman's favourite planet in unsorted list: 2
Element is present at index:  5
<<<<<<< HEAD
'''
=======
'''
>>>>>>> 0f03e71a557e70be0ea4b5bd79ab1ce6104a046c
