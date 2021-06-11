#numbers = [3, 5, 7, 34, 2, 89, 2, 5] 
def num_ques(nums):
	i=0
	c=0
	while i<len(nums):
		if(nums[i]>c):
			c=nums[i]
		i=i+1
	print(c)
num_ques(nums=[3,5,7,34,2,89,2,5])

  