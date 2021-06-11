def function(limit):
    i=0
    s=0
    while i<=limit:
        if i%3==0:
            s=s+i
        elif i%5==0:
            s=s+i
        else:
            pass
        i=i+1
    print(s)
limit=int(input("enter the num "))      
function(limit)