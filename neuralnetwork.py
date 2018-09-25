import numpy as np
from matplotlib import pyplot as plt
# each point is length, width, type (0, 1); 0=blue, 1=red 

data = [[3, 1.5, 1],
		[2,  1,  0],
		[4, 1.5, 1],
		[3,  1,  0],
		[3.5,.5, 1],
		[2,  .5, 0],
		[5.5, 1, 1],
		[1,  1,  0]]
mystery_flower = [4.5, 1]    # we do not now the color of this flower

#print (data[0][1])
#      o    flower type
#     / \   w1, w2, b
#    o   o  length, width


def sigmoid(x):
	return 1/(1+np.exp(-x))
def sigmoid_p(x):    # the derivative of sigmoid
	return sigmoid(x) * (1-sigmoid(x))

T = np.linspace(-6, 6,100) # from -5 to 5 with 10 subdivisions
#print("T  =", T)
Y1 = sigmoid(T)
Y2 = sigmoid_p(T)
#plt.plot(T, Y1, c='r')
#plt.plot(T, Y2, c='b')
#plt.show()

# scatter data
#plt.axis([0, 6, 0, 6])
#plt.grid()
for i in range(len(data)):
	point = data[i]
	color = "r"
	if point[2] == 0:
		color = "b"
#plt.scatter(point[0], point[1], c = color)
#plt.show()

# training loop 
 
# (is going to pick up a random point from the last plot, run it through the network. see what it
#should have been, and that would become our cost. then we are going to take the
# derivative of the cost with respect to the network parameters, use that to 
#update the parameters by subtracting it and that would decrease the cost and
# improves the network prediction for that point. if we see enough points we will
# get better and better predictions)

learning_rate = 0.2  # small farction of derivatives are going to be subtracted
costs = []

w1 =np.random.randn()
w2 =np.random.randn()
b =np.random.randn()

for i in range (50000):
	ri = np.random.randint(len(data))
	point = data[ri]
	
	z = point[0] * w1 + point[1] * w2 + b
	pred = sigmoid(z)
	
	target = point[2]
	cost = np.square(pred - target)
	
	dcost_pred = 2 * (pred - target)# derivative of cost with the respect to prediction
	dpred_dz = sigmoid_p(z)
	
	dz_dw1 = point[0]
	dz_dw2 = point[1]
	dz_db = 1
	
	dcost_dw1 = dcost_pred * dpred_dz * dz_dw1
	dcost_dw2 = dcost_pred * dpred_dz * dz_dw2
	dcost_db = dcost_pred * dpred_dz * dz_db
	
	w1 = w1 - learning_rate * dcost_dw1
	w2 = w2 - learning_rate * dcost_dw2 
	b = b - learning_rate * dcost_db
	
	if i % 100 == 0:
		cost_sum = 0
		for j in range(len(data)):
			point = data[ri]
			
			z = point[0]*w1 + point[1] * w2 + b
			pred = sigmoid(z)
			
			z = mystery_flower[0]*w1 + mystery_flower[1] * w2 + b
			pred = sigmoid(z)
			
			def wich_flower(length, width):
				z = length * w1 + width * w2 + b
				print(z)
				pred = sigmoid(z)
				print (pred)
				if pred<.5:
					print ("blue")
				
				else:
					print ("red")
			
wich_flower(4, 1.5)
#wich_flower(np.inf, np.inf)
