def collect(list1,list2):
    i=0
    e=[]
    c=list1+list2
    while i<len(c):
        if (c[i]  not in e):
          e.append(c[i])
        i=i+1
    e.sort()
    print(e)
list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
collect(list1,list2)
# op= 1,2,5,10,12,13,16,20
# more excercise ques8.