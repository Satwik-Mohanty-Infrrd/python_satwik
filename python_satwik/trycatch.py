try:
	f=open('testfile.txt')
except Exception:
	print('Sorry, this file does not exist')


try:
	f=open('test.rtf')
	var=bad_var
except FileNotFoundError:
	print('Sorry, this file does not exist')
except Exception:
	print('Sorry, something went wrong')


try:
	f=open('test.rtf')
except FileNotFoundError:
	print('Sorry, this file does not exist')
except Exception:
	print('Sorry, something went wrong')
else:
	print(f.read())
	f.close()


try:
	f=open('corrupt.txt')
	if f.name=='corrupt.txt':
		raise Exception
except Exception as e:
	print('Error')
finally:
	print('Execuing finally')
