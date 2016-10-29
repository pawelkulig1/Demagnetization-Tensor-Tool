import math as mt
from formulas import *



#define big structure that is going to be cut
emitter = block(1e-9, 1e-9, 1e-9, 20, 20, 1, 0, 0, 0)
receiver = block(1e-9, 1e-9, 1e-9, 20, 20, 1, 0, 0, 0)


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
		#print(delx, dely, delz)
		
		
		
		#sum up to crate average later
		a11 += calculateNxx(delx, dely, delz, dx, dy, dz, emitter)
		#print(a11)	
		a12 += calculateNxy(delx, dely, delz, dx, dy, dz, emitter)
		a13 += calculateNxy(delx, delz, dely, dx, dz, dy, emitter)
		#a21 = a12
		a22 += calculateNxx(dely, delx, delz, dy, dx, dz, emitter)
		a23 += calculateNxy(dely, delz, delx, dy, dz, dx, emitter)
		#a31 = a13
		#a32 = a23
		a33 += calculateNxx(delz, dely, delx, dz, dy, dx, emitter)

		#print("a22: ",a22)
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
	#print(a22)
	#exit(0)
	#print(a33)
	avgMatrix.append([a11, a12, a13, a12, a22, a23, a13, a23, a33])
	
finalMatrix = [0,0,0,0,0,0,0,0,0]
#print("avgMatrix: ", avgMatrix[0])
#create sum of all matrixes to calculate average
for k in range(len(avgMatrix)):
	for i in range(len(avgMatrix[0])):
		finalMatrix[i] += avgMatrix[k][i]
	
#divide sum by all elements
for k in range(len(avgMatrix[0])):
	finalMatrix[k]/=len(avgMatrix)

#print(len(avgMatrix))

print("[",finalMatrix[0], finalMatrix[1], finalMatrix[2], "]")
print("[",finalMatrix[3], finalMatrix[4], finalMatrix[5], "]")
print("[",finalMatrix[6], finalMatrix[7], finalMatrix[8], "]")

print("suma: ",sum(finalMatrix))

