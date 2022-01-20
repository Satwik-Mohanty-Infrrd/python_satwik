
with open('test.rtf', 'r') as f:
	f_contents= f.read()
	print(f_contents)


with open('test.rtf', 'r') as f:
	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)

	f_contents= f.readline()
	print(f_contents)


f= open('test.rtf', 'r')
print(f.name)
print(f.mode)
f.close()


with open('test.rtf', 'r') as f:

	size=10
	f_contents= f.read(size)
	print(f_contents, end='')

	f.seek(0)

	f_contents= f.read(size)
	print(f_contents)



with open('test2.txt', 'w') as f:
	f.write('Test')
	f.seek(0)
	f.write('R')


with open('test2.txt', 'r') as rf:
	with open('testcopy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)