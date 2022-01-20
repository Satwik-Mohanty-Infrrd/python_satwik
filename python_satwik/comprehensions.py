nums= [1,2,3,4,5,6,7,8,9,10]

l=[]
for n in nums:
	l.append(n)
print(l)

l= [n for n in nums]
print(l)

li= [n*n for n in nums]
print(li)

l1= [n for n in nums if n%2==0]
print(l1)

ml= [(letter, num) for letter in 'abcd' for num in range(4)]
print(ml)

names=['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros=['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
x=zip(names, heros)
print(dict(x))

mydict= {name:hero for name, hero in zip(names,heros) if name!='Peter'}
print(mydict)


num=[1,1,2,3,4,4,5,6,7,7,7,7,9]
myset={n for n in num}
print(myset)

mygen= (n*n for n in nums)

for i in mygen:
	print(i)