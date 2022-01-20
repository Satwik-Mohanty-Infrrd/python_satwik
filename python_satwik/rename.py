import os

os.chdir('/Users/satwikmohanty/Desktop/kiki')

for f in os.listdir():
	print(f)
	print(os.path.splitext(f))

for f in os.listdir():
	f_name, f_ext= os.path.splitext(f)
	print(f_name)