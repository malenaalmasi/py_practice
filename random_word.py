import random
f=open("sowpods.txt","r")
#a= f.read()

#print type(a)
#print f.readlines()
d=f.readlines()
print type(d)
print len(d)
m=len(d)
'''
for x in range(10):
  print random.randint(1,101)
'''


ran=random.randint(0,m)
print d[ran]