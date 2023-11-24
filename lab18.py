def replaceV(S):
  a='aeiouAEIOU'
  b=3
  for i in range(len(S)):
    c=S[i:i+b]
    if len(c)==3:
      e=0
      for j in c:
        if j in a:
          e+=1
      if e==3:
        S=S.replace(c,'_')
  return S

S = input("Enter a string: ")
print(replaceV(S))

'''
output

Enter a string: aaahelooooqueeee
_hel_oq_ee

'''