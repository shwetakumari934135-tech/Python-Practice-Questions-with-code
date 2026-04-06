s=input("Enter string: ") 
v=c=d=sp=0 
for ch in s: 
    if ch.isalpha(): 
        if ch.lower() in 'aeiou': v+=1 
        else: c+=1 
    elif ch.isdigit(): d+=1 
    else: sp+=1 
print(v,c,d,sp) 