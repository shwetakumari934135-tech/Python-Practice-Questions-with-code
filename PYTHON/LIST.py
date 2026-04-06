# CREATING A LIST
a=[1,2,2,4,5]
print(a)   # print(type(a)) CHECKIN TYPE OF a
b=[1,2,2,"Hello","Hello",3.5,True]
print(b)
print(type(b))
# INDEXING OF LIST
print(a[2])
print(b[4])
print(type(b[4]))
print(type(b[5]))
# NEGATIVE INDEX IN LIST
print(a[-2])  # HOW IT WORKS
print(a[len(a)-2]) #First convert negative into positive index.THIS IS HOW NEGATIVE INDEX IN LIST WORKS
# SLICING IN LIST
print(a[0:5:2])
print(a[0:5])