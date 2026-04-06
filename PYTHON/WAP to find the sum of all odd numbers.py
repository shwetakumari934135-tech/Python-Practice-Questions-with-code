# WAP to find the sum of all odd numbers in a list eneterd by the user.
a=list(map(int,input("Enetr the number : ").split()))
sum=0
for i in a:
    if i%2!=0:
        sum+=i
print("Sum of all odd numbers is : ",sum)