# WAP to find the sum of all even numbers in a list entered by the user
a=list(map(int,input("Enter the number : ").split()))
sum=0
for i in a:
    if i%2==0:
        sum+=i
print("Sum of all even number is : ",sum)