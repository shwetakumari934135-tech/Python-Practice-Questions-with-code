print("1.Add 2.Subtract 3.Multiply 4.Divide") 
ch = int(input("Enter choice: ")) 
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
if ch == 1: 
print("Result:", a+b) 
elif ch == 2: 
print("Result:", a-b) 
elif ch == 3: 
print("Result:", a*b) 
elif ch == 4: 
print("Result:", a/b) 
else: 
print("Invalid choice")