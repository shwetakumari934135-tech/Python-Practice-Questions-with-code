# WAP to count the number of even and odd elements in a list entered by the user.
a=list(map(int,input("Enter the number : ").split()))
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Count of even number is : ",even_count)
print("Count of odd number is : ",odd_count)
       