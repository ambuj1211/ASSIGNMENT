L = list(map(int, input().split()))
a=L.count(0)
if a>0:
  for i in range(a):
    L.remove(0)
    L.append(0)
print(L,end='')

'''
output

0 1 2 3 1 4 0 3 0 2
[1, 2, 3, 1, 4, 3, 2, 0, 0, 0]

'''