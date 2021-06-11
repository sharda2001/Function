def sum(numbers):
	i=0
	j=1
	while i<len(numbers):
		j=j*numbers[i]
		i=i+1
	print(j)
sum(numbers=[8,3,7,5])