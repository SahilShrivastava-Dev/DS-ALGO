def sump(n):
    s=0
    for i in range (0,n+1):
        s+=i
    print("the sum is : ",s)    
    return(s)    
x= int(input("enter the number for its sum : "))
sump(x)


