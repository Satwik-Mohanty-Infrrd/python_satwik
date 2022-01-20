num= [1,2,3,4,5]

for n in num:
	if n==3:
		print('Found')
		break
	print(n)

for n in num:
	if n==3:
		print('Found')
		continue
	print(n)


for n in num:
	for letter in 'abc':
		print(n, letter)


for i in range(10):
	print(i)

x=0
while x<10:
	print(x)
	x+=1