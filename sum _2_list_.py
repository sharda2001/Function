def sum(a,b):
	i=0
	c=[]
	while i<len(a):
		d=a[i]+b[i]
		c.append(d)
		i=i+1
	print(c)
sum(a=[50,60,10],b=[10,20,13])
# sum of two list op= 60,80,23