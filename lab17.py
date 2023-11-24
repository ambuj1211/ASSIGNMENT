input_Tuple= input("Enter a tuple: ")
tuple_ = tuple(map(int, input_Tuple.split(',')))
tem = []
for i in tuple_:
    tem.append(i**2)

tuple_2 = tuple(tem)
out_tuple = tuple_ + tuple_2
print(out_tuple)