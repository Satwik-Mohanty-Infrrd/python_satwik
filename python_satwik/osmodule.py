import os
#print(dir(os))

print(os.getcwd())

#os command to create deep directories
#os.makedirs('OS-Demo-2/Sub-Dir-1')


#os command to rename files
#os.rename('demo.rtf','test.rtf')

#Printing the properties of the file
print(os.stat('test.rtf'))


from datetime import datetime
time= os.stat('test.rtf').st_mtime
print(datetime.fromtimestamp(time))
#print(os.listdir())


#To Get a walkthrough of all the files in the current working directory
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	print('Current path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)
	print()

#Print Home directory Path
print(os.environ.get('HOME'))

#os.join method
file_path= os.path.join(os.environ.get('HOME'), 'test.rtf')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

