import math as mt
import formulas

class block:
	def __init__(self, swidth=50, sdepth=10, sheight=10, wElements = 10, dElements=10, hElements=10, xpoz=0, ypoz=0, zpoz=0):
		#define central cordinates of block
		self.xpoz = xpoz
		self.ypoz = ypoz
		self.zpoz = zpoz

		self.widthSmall = swidth
		self.depthSmall = sdepth
		self.heightSmall = sheight
		
		self.wElements = wElements
		self.dElements = dElements
		self.hElements = hElements
		
		#calculate size of block in m.
		
		self.calcBigSize()
		self.nElements = int(round((self.width*self.depth*self.height)/(self.widthSmall*self.depthSmall*self.heightSmall)))
		
		
		#calculate big object size
	def calcBigSize(self):
		self.width = self.widthSmall*self.wElements
		self.depth = self.depthSmall*self.dElements
		self.height = self.heightSmall*self.hElements
		
		
	#returns size of small blocks created from origin block
	def getSmallSize(self):
		return self.widthSmall, self.depthSmall, self.heightSmall
		
	'''
		return x,y,z cordinates for small block with given number, numbers goes from bottom-front-left corner to top-back-right (from 0 to (n-1)) it can be understood as 2-dimensional arrays stacked level by level
	'''
	def smallPoz(self, number): #return cordinates of smallBlock center
		if self.width==0:
			raise NameError("Probably block smallSize was not called")
		
		#calculate position of block in my cordinates height, depth, width
		blocksPerLevel = round(self.width/self.widthSmall * self.depth/self.depthSmall)
		blocksPerWidth = round(self.width/self.widthSmall)
		blocksPerDepth = round(self.depth/self.depthSmall)
		

		level = mt.floor(number/blocksPerLevel)
		number = number - level*blocksPerLevel
		
		depthLevel = mt.floor(number/blocksPerWidth)
		number = number - depthLevel*blocksPerWidth
		
		widthLevel = number
		number = number - widthLevel
		
		if(number!=0): #it should never be true otherwise better to raise exception cause weird things may happen
			raise NameError("Error while calculating poz of element")

		xpozSmall = self.xpoz+widthLevel*self.widthSmall + 0.5*self.widthSmall
		ypozSmall = self.ypoz+depthLevel*self.depthSmall + 0.5*self.depthSmall
		zpozSmall = self.zpoz+level*self.heightSmall + 0.5*self.heightSmall
				
		return xpozSmall, ypozSmall, zpozSmall

class smallBlock:
	def __init__(self, xpoz, ypoz, zpoz, width, depth, height):
		#define central cordinates of block
		self.xpoz = xpoz
		self.ypoz = ypoz
		self.zpoz = zpoz

		#define size of block in nm.
		self.width = width
		self.height = height
		self.depth = depth
	
	def getCoordinates(self):
		return self.xpoz, self.ypoz, self.zpoz

	#overloading addition returns delta(x), delta(y), delta(z)
	def __add__(self, other):
		return abs(self.xpoz-other.xpoz), abs(self.ypoz-other.ypoz), abs(self.zpoz-other.zpoz)
		
	#overloading multiplication to get distance between two blocks in nm.	
	def __mul__(self, other): 
		return mt.sqrt((self.xpoz-other.xpoz)**2 + (self.ypoz-other.ypoz)**2 + (self.zpoz-other.zpoz)**2)


#define big structure that is going to be cut
emitter = block(2e-10, 1e-9, 1e-9, 200, 1, 1)
receiver = block(2e-10, 1e-9, 1e-9, 200, 1, 1)


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


print(receiverDivided[0]+emitterDivided[199])




avgMatrix = []
for j in range(receiver.nElements):
	
	#print(j, "/", receiver.nElements)
	#print(".", end="", flush=True)
	S1 = []
	S2 = []
	S3 = []
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
				
		
		
		
		S1.append([
			[delx + dx, dely, delz],
			[delx - dx, dely, delz], 
			[delx, dely + dy, delz],
			[delx, dely - dy, delz],
			[delx, dely, delz + dz],
			[delx, dely, delz - dz]
		])
		
		S2.append([
			[delx + dx, dely + dy, delz],
			[delx - dx, dely + dy, delz],
			[delx + dx, dely - dy, delz],
			[delx - dx, dely - dy, delz],
			[delx, dely + dy, delz + dz],
			[delx, dely - dy, delz + dz],
			[delx, dely + dy, delz - dz],
			[delx, dely - dy, delz - dz],
			[delx + dx, dely, delz + dz],
			[delx - dx, dely, delz + dz],
			[delx + dx, dely, delz - dz],
			[delx - dx, dely, delz - dz]
		])

		S3.append([
			[delx + dx, dely + dy, delz + dz],
			[delx - dx, dely + dy, delz + dz],
			[delx - dx, dely - dy, delz + dz],
			[delx - dx, dely - dy, delz - dz],
			[delx + dx, dely - dy, delz - dz],
			[delx + dx, dely + dy, delz - dz],
			[delx + dx, dely + dy, delz + dz],
			[delx - dx, dely + dy, delz - dz]
		])
		
		#part of code to secure non existing blocks - there is risk that we will count magnetic field to block that doesn't exist especially near border blocks so we have to get rid of that part of S vector
		
		S1deletion = []
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
			
		
		print(dx, dy,dz)
		#sum up to crate average later
		a11 += formulas.calculateNxx(delx, dely, delz, dx, dy, dz, S1[i], S2[i], S3[i])
		print("Nxx(",delx, dely, delz, dx, dy, dz, S1[i], S2[i], S3[i], ")")
		if a11>25000:
			#print("weird moment - 1:", delx, dely, delz, dx, dy, dz, S1[i-1], S2[i-1], S3[i-1])
			
			print(formulas.calculateNxx(delx, dely, delz, dx, dy, dz, S1[i], S2[i], S3[i]))
			
			exit(0)
		a12 += formulas.calculateNxy(delx, dely, delz, dx, dy, dz, S1[i], S2[i], S3[i])
		a13 += formulas.calculateNxy(delx, delz, dely, dx, dz, dy, S1[i], S2[i], S3[i])
		#a21 = a12
		a22 += formulas.calculateNxx(dely, delx, delz, dy, dx, dz, S1[i], S2[i], S3[i])
		a23 += formulas.calculateNxy(dely, delz, delx, dy, dz, dx, S1[i], S2[i], S3[i])
		#a31 = a13
		#a32 = a23
		a33 += formulas.calculateNxx(delz, dely, delx, dz, dy, dx, S1[i], S2[i], S3[i])
		print ("a11: ",a11)
		#N = [a11, a12, a13, a12, a22, a23, a13, a23, a33]
	print("======================")
	#print ("Em el: ", emitter.nElements)
	a11=a11/emitter.nElements
	a12=a12/emitter.nElements
	a13=a13/emitter.nElements
	a22=a22/emitter.nElements
	a23=a23/emitter.nElements
	a33=a33/emitter.nElements
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
