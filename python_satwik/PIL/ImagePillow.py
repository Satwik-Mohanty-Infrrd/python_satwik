from PIL import Image
import os

size= (300, 300)
for f in os.listdir('.'):
	if f.endswith('.jpeg'):
		i= Image.open(f)
		fn,fext= os.path.splitext(f)
		i.thumbnail(size)
		i.save('300/{}_300{}'.format(fn, fext))
		#f= Image.open(f)
		#fn, fext= os.path.splitext(f)
		#f.save('pngs/{}.png'.format(fn))



#image1= Image.open('1.jpeg')
#image1.show()

#image1.save('1.png')