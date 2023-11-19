# Question 4

a = [0,1]
for i in range(int(input("Give an integer: "))):
    print(a[i])
    if(i>0):
        a.append(a[i]+a[i-1])