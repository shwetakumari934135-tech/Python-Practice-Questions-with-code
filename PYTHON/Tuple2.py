# Tuple2
tup=(1,2,1,4,1,1)
temp=list(tup)     # coverting tuple into list to perform operation on tuple
temp[0]=90
temp[4]=80
tup=tuple(temp)
print(tup)
print(tup.count(1))
print(tup.index(4))
