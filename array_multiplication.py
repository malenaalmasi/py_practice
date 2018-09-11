import sys
import numpy as np
input= sys.argv
print input
input.pop(0)
print input


A= []
B= []
C=[]
 



m=len(input)
print "m=",m
for i in range(0,m):
	#print "i=", i, (m/2)
	if i< (m/2):
		A.append(float(input[i]))
		
	else:
		B.append(float(input[i]))
	
l= np.sqrt(m/2)		
for k in range(0,l):
	A[0]*B[0]+A[1]*B[2]
	
	
