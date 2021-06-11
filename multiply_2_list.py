def calculator(num1,num2):
	c=[]
	i=0
	while (i< len(num1)):
		multi=(num1[i]*num2[i])
		c.append(multi)
		i=i+1
	print(c)
calculator(num1=[5,6,7,2],num2=[34,30,45,2])
# multiply of two list in function op- 170,180,315,4