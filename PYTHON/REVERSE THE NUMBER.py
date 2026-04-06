#  REVERSE THE NUMBER
a=int(input("Enter the number : "))
reverse=0
while a>0:
    num=a%10
    reverse=reverse*10+num
    a=a//10
    print("Reversed number : ",reverse)