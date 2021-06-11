def min(list):
    i=0
    min=list[0]
    while i<len(list):
        if list[i]<min:
            min=list[i]
        i=i+1
    print(min)
min(list=[1,4,87,5,80])


