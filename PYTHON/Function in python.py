# Function in pyhton
def hello():
    print("Hello World")
hello()
#  function with parametr
def greet(name):
    print("Hello ",name)
greet("Shweta")
greet("World")
#Function with multiple values
def add(a,b):
    print(a+b)
add(5,7)
add(8,9)
add(15,25)
add(25,15)
#return keyword
def add(a,b):
    return a+b
result=add(4,5)
print(result)

# check even or odd using function
def is_even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(is_even(25))
print(is_even(20))
print(is_even(30))
print(is_even(25))
# square of number
def square(n):
    return n*n
print(square(5))
print(square(2))
# largest number
def LargestNumber(a,b):
    if a>b:
        return a
    else:
        return b
print(LargestNumber(10,20))
print(LargestNumber(55,60))
# Positive/Negative/Zero check
def Check_Number(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "zero"
print(Check_Number(20))
print(Check_Number(-23))
print(Check_Number(35))
print(Check_Number(0))
#Simple Calculator
def Calculator(a,b):
    return a+b,a-b,a*b,a/b
add,sub,mul,div=Calculator(10,5)
print("Add :",add)
print("Add :",sub)
print("Add :",mul)
print("Add :",div)
# Even number count
def count_even(lst):
    count=0
    for i in lst:
        if i%2==0:
          count+=1
    return count
 
print(count_even([1,2,3,4,5,6,8]))

