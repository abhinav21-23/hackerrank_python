n=int(input())
if n>20:
    if n%2==0:
        print("Not Weird")
    else:
        print("Weird")
elif n==20:
    print("Weird")    
else:
    if n%2!=0:
        print("Weird")
    elif n==18:
        print("Weird")
    else:
        print("Not Weird")
