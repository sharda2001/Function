def divisiable(num):
    i=0
    while i<=1000:
        if i%3==0:
            print("nav")
        elif i%7==0:
            print("gurukul")
        elif i%21==0:
            print('navgurukul')
        else:
            pass
        i=i+1
divisiable(num=int(input("enter the no.")))
        
