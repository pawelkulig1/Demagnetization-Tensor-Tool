import math as mt
from formulas import *



#define big structure that is going to be cut
emitter = block(2e-10, 1e-9, 1e-9, 1, 1, 1, 1e-8, 0, 0)
receiver = block(2e-10, 1e-9, 1e-9, 1, 1, 1, 0, 0, 0)


#for each small part create object

	
emitterDivided = []
for i in range(emitter.nElements):
	x, y, z = emitter.smallPoz(i)
	#print("%.12f" %x, "%.12f" %y, "%.12f" %z,)
	dx, dy, dz = emitter.getSmallSize()
	#print("%.12f" %dx, "%.12f" %dy, "%.12f" %dz)
	emitterDivided.append(smallBlock(x,y,z, dx, dy, dz))

receiverDivided = []
for i in range(receiver.nElements):
	x, y, z = receiver.smallPoz(i)
	dx, dy, dz = receiver.getSmallSize()
	receiverDivided.append(smallBlock(x,y,z, dx, dy, dz))



print (receiver.nElements, emitter.nElements, emitter.getSmallSize())
print (receiver.width, receiver.depth, receiver.height)

#Create helpful S1, S2, S3 vectors for all cells


#print(receiverDivided[0]+emitterDivided[199])




avgMatrix = []
for j in range(receiver.nElements):
	
	print(j, "/", receiver.nElements)
	#print(".", end="", flush=True)
	a11 = 0
	a12 = 0
	a13 = 0
	a22 = 0
	a23 = 0
	a33 = 0
	#print (a11)
	
	for i in range(emitter.nElements):
		
		delx, dely, delz = (receiverDivided[j]+emitterDivided[i])
		
		dx = emitterDivided[i].width
		dy = emitterDivided[i].depth
		dz = emitterDivided[i].height
		
		
		'''S1deletion = []
		S2deletion = []
		S3deletion = []
		
		if emitterDivided[i].xpoz-dx<emitter.xpoz:
			S1deletion.append(1)
			
			S2deletion.append(1)
			S2deletion.append(3)
			S2deletion.append(9)
			S2deletion.append(11)
			
			S2deletion.append(1)
			S2deletion.append(2)
			S2deletion.append(3)
			S2deletion.append(7)

		if emitterDivided[i].xpoz+dx>emitter.xpoz+emitter.width:
			S1deletion.append(0)
			S2deletion.append(0)
			S2deletion.append(2)
			S2deletion.append(8)
			S2deletion.append(10)
			S3deletion.append(0)
			S3deletion.append(4)
			S3deletion.append(5)
			S3deletion.append(6)
		
		if emitterDivided[i].ypoz-dy<emitter.ypoz:
			S1deletion.append(3)
			S2deletion.append(2)
			S2deletion.append(3)
			S2deletion.append(5)
			S2deletion.append(7)
			S3deletion.append(2)
			S3deletion.append(3)
			S3deletion.append(4)
			
		if emitterDivided[i].ypoz+dy>emitter.ypoz+emitter.depth:
			S1deletion.append(2)
			S2deletion.append(0)
			S2deletion.append(1)
			S2deletion.append(4)
			S2deletion.append(6)
			S3deletion.append(0)
			S3deletion.append(1)
			S3deletion.append(5)
			S3deletion.append(6)
			S3deletion.append(7)
		
		if emitterDivided[i].zpoz-dz<emitter.zpoz:
			S1deletion.append(5)
			S2deletion.append(6)
			S2deletion.append(7)
			S2deletion.append(10)
			S2deletion.append(11)
			S3deletion.append(3)
			S3deletion.append(4)
			S3deletion.append(5)
			S3deletion.append(7)
			
		if emitterDivided[i].zpoz+dz>emitter.zpoz+emitter.height:
			S1deletion.append(4)
			S2deletion.append(4)
			S2deletion.append(5)
			S2deletion.append(8)
			S2deletion.append(9)
			S3deletion.append(0)
			S3deletion.append(1)
			S3deletion.append(2)
			S3deletion.append(6)
		
		#getting rid of repeating elements
		S1deletion = list(set(S1deletion))
		S2deletion = list(set(S2deletion))
		S3deletion = list(set(S3deletion))
		
		S1deletion.sort()
		S2deletion.sort()
		S3deletion.sort()
		
		#reverse vectors to avoid mess with changing array indexes now we will delete from last element not from first
		S1deletion.reverse()
		S2deletion.reverse()
		S3deletion.reverse()
		
		
		#delete those outside of block object
		
		for k in S1deletion:
			#print(S1[i][k])
			del(S1[i][k])
			
			
		for k in S2deletion:
			#print(S2[i][k])
			del(S2[i][k])
			
		for k in S3deletion:
			del(S3[i][k])
		#print (S1deletion, S2deletion, S3deletion)
		#exit()
		'''
		
		#sum up to crate average later
		a11 += calculateNxx(delx, dely, delz, dx, dy, dz, emitter, i)
		#print(a11)	
		a12 += calculateNxy(delx, dely, delz, dx, dy, dz, emitter, i)
		a13 += calculateNxy(delx, delz, dely, dx, dz, dy, emitter, i)
		#a21 = a12
		a22 += calculateNxx(dely, delx, delz, dy, dx, dz, emitter, i)
		a23 += calculateNxy(dely, delz, delx, dy, dz, dx, emitter, i)
		#a31 = a13
		#a32 = a23
		a33 += calculateNxx(delz, dely, delx, dz, dy, dx, emitter, i)
		print("a11: ",a11)
		#print(delx, dely, delz)
		#N = [a11, a12, a13, a12, a22, a23, a13, a23, a33]
	#print("======================")
	
	#print ("Em el: ", emitter.nElements)
	a11=a11/emitter.nElements
	a12=a12/emitter.nElements
	a13=a13/emitter.nElements
	a22=a22/emitter.nElements
	a23=a23/emitter.nElements
	a33=a33/emitter.nElements
	#print(a11)
	exit(0)
	#print(a33)
	avgMatrix.append([a11, a12, a13, a12, a22, a23, a13, a23, a33])
	
finalMatrix = [0,0,0,0,0,0,0,0,0]
print("avgMatrix: ", avgMatrix[0])
#create sum of all matrixes to calculate average
for k in range(len(avgMatrix)):
	for i in range(len(avgMatrix[0])):
		finalMatrix[i] += avgMatrix[k][i]
	
#divide sum by all elements
for k in range(len(avgMatrix[0])):
	finalMatrix[k]/=len(avgMatrix)

print(len(avgMatrix))

print(finalMatrix)
