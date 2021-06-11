def duplicate(a):
    i=0
    b=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i=i+1
    print(b)
a=["sharda","suman","sharda","suman"]
duplicate(a)

