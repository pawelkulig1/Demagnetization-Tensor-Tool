import math as mt
import formulas

class block:
	def __init__(self, width=50, depth=10, height=10, nElements = 1000, xpoz=0, ypoz=0, zpoz=0):
		#define central cordinates of block
		self.xpoz = xpoz
		self.ypoz = ypoz
		self.zpoz = zpoz

		#define size of block in nm.
		self.width = width
		self.height = height
		self.depth = depth

		#how many pieces to consider
		self.nElements = nElements
		self.calcSmallSize()
		
		
		
	def calcSmallSize(self):
		ratio = self.nElements**(1/3)
	
		self.widthSmall = self.width/ratio;
		self.heightSmall = self.height/ratio;
		self.depthSmall = self.depth/ratio;
	
	#returns size of small blocks created from origin block
	def getSmallSize(self):
		return self.widthSmall, self.depthSmall, self.heightSmall
		
	'''
		return x,y,z cordinates for small block with given number, numbers goes from bottom-front-left corner to top-back-right (from 0 to (n-1)) it can be understood as 2-dimensional arrays stacked level by level
	'''
	def smallPoz(self, number):
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


#deleting not existing elements from Sn vectors (when cell is on corner or in wall it has less neighbours
def deleteNotExisting(Sn, block1):
	source = block1
	
	for j in range(len(Sn)):
		counter = 0
		for i in range(len(Sn[j])):
			if (Sn[j][counter][0]<source.xpoz or Sn[j][counter][0]>(source.xpoz+source.width)) or (Sn[j][counter][1]<source.ypoz or Sn[j][counter][1]>(source.ypoz+source.depth)) or (Sn[j][counter][2]<source.zpoz or Sn[j][counter][2]>(source.zpoz+source.height)):
				del(Sn[j][counter])
				counter-=1
				#continue
			
			counter+=1
			


#define big structure that is goind to be cut
emitter = block(50,10,10,1000,0,0,0)
receiver = block(50, 10, 10, 1000, 0, -20 , 0)


#for each small part create object

	
emitterDivided = []
for i in range(emitter.nElements):
	x, y, z = emitter.smallPoz(i)
	dx, dy, dz = emitter.getSmallSize()
	emitterDivided.append(smallBlock(x,y,z, dx, dy, dz))

receiverDivided = []
for i in range(receiver.nElements):
	x, y, z = receiver.smallPoz(i)
	dx, dy, dz = receiver.getSmallSize()
	receiverDivided.append(smallBlock(x,y,z, dx, dy, dz))


#Create helpful S1, S2, S3 vectors for all cells

S1 = []
S2 = []
S3 = []



for j in range(1):#range(receiver.nElements):
	
	#Nmatrix = []
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
		
		print(S1[0])
		
		#deleteNotExisting(S1, emitter)
		#deleteNotExisting(S2, emitter)
		#deleteNotExisting(S3, emitter)NOT WORKING
		
		a11 = formulas.calculateNxx(delx, dely, delz, dx, dy, dz, S1[i], S2[i], S3[i])
		a12 = formulas.calculateNxy(delx, dely, delz, dx, dy, dz, S1[i], S2[i], S3[i])
		a13 = formulas.calculateNxy(delx, delz, dely, dx, dz, dy, S1[i], S2[i], S3[i])
		#a21 = a12
		a22 = formulas.calculateNxx(dely, delx, delz, dy, dx, dz, S1[i], S2[i], S3[i])
		a23 = formulas.calculateNxy(dely, delz, delx, dy, dz, dx, S1[i], S2[i], S3[i])
		#a31 = a13
		#a32 = a23
		a33 = formulas.calculateNxx(delz, dely, delx, dz, dy, dx, S1[i], S2[i], S3[i])
		N = [a11, a12, a13, a12, a22, a23, a13, a23, a33]
	
	


#print (emitterDivided[0].zpoz, receiverDivided[0].zpoz)
#print(emitterDivided[0]+receiverDivided[0])

#Create helpful S1, S2, S3 vectors for all cells




Nxx = []
Nxy = []


#print(S1[0])
#formulas.fsum(S1[0])





