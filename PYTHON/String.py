#  String

a="World"
print(a)
print("Hello "+a)
# Print HE said, "I want to eat an apple."
apple='"I want to eat an apple."'
print("He said, "+apple)    #Metho 1
apple='HE said, "I want to eat an apple."'
print(apple)     #Metho 2
apple="HE said, \"I want to eat an apple."
print(apple)      #Metho 3
#  Print Multiple line of string in a single variable.
temp='''Hello guys,
My name is Shweta Kumari.
I am a student.'''
print(temp)
#  Print the each alphabet of the string.
name="HEllo"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Insted of printing one by one we simple use a for loop to acces all the alphabet of string.
for alphabet in name:
    print(alphabet)