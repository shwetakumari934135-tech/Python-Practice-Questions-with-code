# Tuple 
tup=(1,2,3,4,"hello",1.25,True)
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])
print("Length of tuple is : ",len(tup))
print(tup[len(tup)-1])
print(tup[-1])
print(tup[1:3])
print(tup[1:4:2])
if 10 in tup:
    print("Yes it is in tuple")
else:
    print("No it is not in tuple")    
print(tup[len(tup)-2])
tup1=tup[1:4]
print(tup1)



