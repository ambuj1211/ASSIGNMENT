s = input("Enter a string containing 0 and 1 only : ")
sum = 0
tem = 0
for i in s:
    if i =='0':
        tem +=1
    else:
        if tem>sum:
            sum = tem
        tem = 0

if tem>sum:
    sum = tem
print("Length of largest streak 0s = ",sum)


'''
output

Enter a string containing 0 and 1 only : 100010010000001
Length of largest streak 0s =  6

'''