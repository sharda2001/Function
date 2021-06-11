def factorial_number(n):
	fac=1
	while n>0:
		fac=fac*n
		n=n-1
	print(fac)
factorial_number(n=int(input('enter the number')))
