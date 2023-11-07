num=int(input("enter the number"))
count=0
i=2
if num==1:
    print("it is unique no")
else:
    while(i<=num):
        if num%i==0:
            count+=1
        i+=1
    if count==1:
        print("prime no")
    else:
        print("not a prime no")
