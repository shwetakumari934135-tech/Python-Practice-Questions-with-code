# WAP to display all even numbers from a list entered by the user.
a = list(map(int,input("Enter the number : ").split()))
for i in a:
    if i % 2 == 0:
        print(i)
        