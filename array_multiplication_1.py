import sys
import numpy as np

### python array_multiplication_1.py 1 1 0 1 2 2 2 0
### python array_multiplication_1.py 1 1 0 1 2 2 2 0 1 1 2 1 1 2 1 2 1 0 

input= sys.argv
print input
input.pop(0)
m=len(input)
print "m=", m

if m == 8 or m==18:
	if m==8:
		dim=2
	elif m==18:
		dim=3
	
	
	print input

	A= []
	B= []
	C=[]

	for i in range(0,m):
		if i< (m/2):
			A.append(float(input[i]))
			
		else:
			B.append(float(input[i]))
	#print "A=", A
	#print "B=", B
	
	
	A = np.reshape (A,(dim,dim))
	B = np.reshape (B, (dim,dim))
	print "A = ", A
	print "B = ", B
			
	C = np.matmul (A,B)
	print "C=", C
else:
	print"error"
