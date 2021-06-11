def variable(a,b,c):    
    if a>b  and a>c:
        print("a is greater")
    elif b>a and a>c:
        print("b is greter")
    elif c>a and  c>a:
     print("c is greater")
    else:
        pass
a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
variable(a,b,c)
