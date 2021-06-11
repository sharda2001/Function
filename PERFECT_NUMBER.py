def perfect (a):
    sum=0
    i=1
    while i< a:
        if a%i==0:
            sum=sum+i
        i=i+1
    return(sum==a)  
num= int(input("enter the number"))
if perfect(num):
    print(num, "it is perfect number")
else:
    print(num, "it is not perfect number")
