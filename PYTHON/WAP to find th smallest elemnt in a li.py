#  WAP to find th smallest elemnt in a list entered by the user.
a=list(map(int,input("Enter the number : ").split()))
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)