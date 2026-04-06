#  Dictionnaries Method
ep1={122:62,568:72,963:68,859:76,657:69}
ep2={358:90,964:80,934:95}
ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)
ep2.pop(358)
print(ep2)
# popitem method remobves the last key value pairs from the dictionary
ep3={100:96,896:85,7745:63}
ep3.popitem()
print(ep3)

