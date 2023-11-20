s = input("Enter your message: ")
ans = ""
for i in s:
    if ord(i) >=65 and ord(i)< (65+26):
        if ord(i)-3 < 65:
            ans = ans+(chr(ord(i)+23))
        else:
            ans =ans+(chr(ord(i) - 3))
    else:
        if i == " ":
            ans += " "
        if ord(i) >=97 and ord(i)< (97+26):
            if ord(i)-2 < 97:
                ans = ans+(chr(ord(i)+24))
            else:
                ans +=(chr(ord(i) - 2))
print(ans)

''' 
output 1

Enter your message: Hello Juliet
Ecjjm Gsjgcr



output 2

Enter your message: Hello World
Ecjjm Tmpjb

'''