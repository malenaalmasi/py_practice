from PIL import Image
import random

x = int(input("enter the  number of image's width pixels =", ))
y = int(input("enter the  number of image's length pixels =", ))
z = int(input("how many images do you prefer? =", ))
'''
im = Image.new('RGBA', (x, y), (255, 255, 255, 255)) 
#print (im)
px = im.load()
#print  (px)

#px[0,0] = (0,0,0,0)
#print (px[0,0])
'''

no_pix = int((x*y)/10)  # change 10 percent of each image's pixels to black

for m in range (0,z):
	im = Image.new('RGBA', (x, y), (255, 255, 255, 255)) 
	px = im.load()
	
	
	for k in range(0,no_pix):     
		i = random.randint(0, x-1)
		j = random.randint(0, y-1)
		px[i,j] = (0,0,0,0)
	
		file_name = 'im_'+ str(m)+'.bmp'
		flag = random.randint(0,1)   # for half of the all images  make a line   
	
	if flag == 0:
		for r in range(0,x):
			px[r,j] = (0,0,0,0)

		file_name = 'Him_'+ str(m)+'.bmp'
	
	#im.show()
	im.save(file_name)