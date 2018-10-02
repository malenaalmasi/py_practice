
from PIL import Image
from os import walk
import numpy as np

def test_image(l):
	for j in range (0, size):
		z = l[j]*w[j]
		z +=b
		pred = sigmoid(z)
	print('z', z)
	print ('pred',pred)
	if pred < .5:
		print ("Ther is no line")
		
	else:
		print ("There is a line ")


f = []
for (dirpath, dirnames, filenames) in walk('.'):
	f.extend(filenames)
print (f)

f2 = []
for i in range (0,len(f)):
	if f[i][-3:] == 'bmp': 
		f2.append(f[i])
print ('f2 = ',f2)

data = [] 

for j in range (0, len(f2)):	
	im = Image.open(f2[j])
	px = im.load()
	size = im.size[0]*im.size[1]
	pix_val = list(im.getdata())
	#print (pix_val[0])
	data_code = []
	for k in range (0,size):
		color_code = ""
		for c in range (0,len(pix_val[k])):
			color_code += (str(pix_val[k][c]))
		color_code_f = float(color_code)
		color_code_1 = color_code_f/255255255 		#255255255 is becauseof (255,255,255) for white
		#print (color_code_1)
		data_code.append(color_code_1)
		
	#print ('dddd = ',data_code)
	#print (f2[j][0])
	if f2[j][0] == 'H':
		data_code.append(1)
		data.append(data_code)
	elif f2[j][0] == 'i':
		data_code.append(0)
		data.append(data_code)
	
	elif f2[j][0] == 'P':
		mystery_image = data_code
		f2.pop(j)
		#print( 'MMMMMM = ', data_code[j])
	#print ('f 22 ==== ',f2)
	
	#print (data)
print (len(data))
def sigmoid(x):
	return 1/(1+np.exp(-x))
def sigmoid_p(x):    # the derivative of sigmoid
	return sigmoid(x) * (1-sigmoid(x))


learning_rate = 0.01  # small farction of derivatives are going to be subtracted
costs = []

w = []

for i in range(0, size):
	a =np.random.randn()
	w.append(a)
#print (w)
b =np.random.randn()
#print(b)

for i in range (0,100000):   # repeatation**********************************
	
	ri = np.random.randint(len(data))
	point = data[ri]
	z = 0
	for r in range (0, size):
		z = data[ri][r] * w[r] 
		z += z
		z += b
		pred = sigmoid(z)
	
	#print (size)
	#print (len(point))
	target = point[size]
	cost = np.square(pred - target)
	print (i , ' = ' , cost , ' / ', pred , ' / ', target)
	dcost_pred = 2 * (pred - target)# derivative of cost with the respect to prediction
	dpred_dz = sigmoid_p(z)
	
	
	dz_dw = []
	dcost_dw = []
	w1 = 0
	for i in range (0, size):
		dz_dw.append(point[i])
		dcost_dw1 = dcost_pred * dpred_dz * point[i]
		dcost_dw.append(dcost_dw1)
		w[i]= w[i] - learning_rate * dcost_dw1
		
	dz_db = 1
	dcost_db = dcost_pred * dpred_dz * dz_db
	b = b - learning_rate * dcost_db
	
test_image(mystery_image)

file = open('w_b.txt', 'w')
for i in range (0,len(w)):
	file.writelines(str(w[i]))
	file.writelines('	')
file.writelines(str(b))
file.close()
