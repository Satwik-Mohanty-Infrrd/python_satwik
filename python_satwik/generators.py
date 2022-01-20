def square_numbers(nums):
	res=[]
	for i in nums:
		res.append(i*i)
	return res

my_nums= square_numbers([1,2,3,4,5])
print(my_nums)


def square(nums):
	for i in nums:
		yield(i*i)

mynums= square([1,2,3,4,5])
print(next(mynums))
print(next(mynums))
print(next(mynums))
print(next(mynums))
print(next(mynums))
