import math as mt


class block:
	def __init__(self, swidth=1, sdepth=1, sheight=1, wElements = 10, dElements=10, hElements=10, xpoz=0, ypoz=0, zpoz=0):
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
	
	
	def ifSmallBlockExists(self, x,y,z):
		#print(self.xpoz)
		if x>self.width+self.xpoz-(self.widthSmall/2):
			return 0
		
		if x<self.xpoz+(self.widthSmall/2):
			return 0
		
		if y>self.depth+self.ypoz-(self.depthSmall/2):
			return 0
		
		if y<self.ypoz+(self.depthSmall/2):
			return 0
	
		if z>self.height+self.zpoz-(self.heightSmall/2):
			return 0
		
		if z<self.zpoz+(self.heightSmall/2):
			return 0
		
		return 1

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

def radius(x,y,z):
	return mt.sqrt(x**2 + y**2 + z**2)
	
def f(x,y,z):
	R = radius(x, y, z)
	
	'''return (
		0.5*y*(z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
		+ 0.5*z*(y**2 - x**2) * mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		- x*y*z*((y*z)/(x*R))
		+ (1/6)*R*(2*x**2 - y**2 - z**2)
	)'''
	
	#solving 0 division problem here
		
	if x==0 and z==0 or y==0:
		part1=0
	else:
		part1 = 0.5*y*(z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
	
	if x==0 and y==0 or z==0:
		part2=0
	else:
		part2 = 0.5*z*(y**2 - x**2) * mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		
	if x==0 or y==0 or z==0:
		part3 = 0
	else:
		part3 = x*y*z*mt.atan((y*z)/(x*R))
	
	#solving 0 division problem here
	
	part4 = (1/6.0)*R*(2*x**2 - y**2 - z**2)
	
	return part1 + part2 - part3 + part4
	

def g(x,y,z):
	R = radius(x, y, z)
	'''
	return (
		x*y*z*mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		+ (1/6)*y*(3*z**2 - y**2) * mt.asinh(x/(mt.sqrt(y**2 + z**2)))
		+ (1/6)*x*(3*z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
		- 0.5*y**2*z * mt.atan((x*z)/(y*R))
		- 0.5*x**2*z * mt.atan((y*z)/(x*R))
		- (1/6)*z**3 * mt.atan((x*y)/(z*R))
		- (1/3)*x*y*R
	)'''
		
	if x == 0 and y==0:
		part1 = 0
	else:	
		part1 = x*y*z*mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		
	if y==0 and z==0:
		part2 = 0
	else:
		part2 = (1/6.0)*y*(3*z**2 - y**2) * mt.asinh(x/(mt.sqrt(y**2 + z**2)))
		
	if x==0 and z==0:
		part3 = 0
	else:
		part3 =(1/6.0)*x*(3*z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
	
	if y==0:
		part4 = 0
	else:
		part4 = 0.5*(y**2)*z * mt.atan((x*z)/(y*R))
		
	if x==0:
		part5 = 0
	else:
		part5 = 0.5*(x**2)*z * mt.atan((y*z)/(x*R))
		
	if z==0:
		part6 = 0
	else:
		part6 = (1/6.0)*z**3 * mt.atan((x*y)/(z*R))
		
	part7 = (1/3.0)*x*y*R
	
	return part1+part2+part3-part4-part5-part6-part7

#dist0 used to recognise if this is S1, S2 or S3 vector Block
def dist0(x,y,z):
	w = mt.sqrt(x**2+y**2+z**2)
	#print(w)
	if w==1:
		return 1
	if w>1 and w<mt.sqrt(3)-0.01:
		return 2
	else:
		return 3

def generateSVectors(delx, dely, delz, dx, dy, dz, emitter, i):
	S1 = []
	S2 = []
	S3 = []

	'''xmax=emitter.width+emitter.xpoz
	xmin=emitter.xpoz
	ymax=emitter.depth+emitter.ypoz
	ymin=emitter.ypoz
	zmax=emitter.height+emitter.zpoz
	zmin=emitter.zpoz

	smallBx, smallBy, smallBz = emitter.smallPoz(i)
	#print(smallBx, smallBy, smallBz)
	
	emitdx = emitter.widthSmall
	emitdy = emitter.depthSmall
	emitdz = emitter.heightSmall

	#print(emitdx, emitdy, emitdz)

	for x in range(-1,2,1):
		for y in range(-1,2,1):
			for z in range(-1,2,1):
				if x==0 and y==0 and z==0:
					continue

				if smallBx+emitdx*x<xmax and smallBx + x*emitdx>xmin and smallBy+emitdy*y<ymax and smallBy+emitdy*y>ymin and smallBz+emitdz*z<zmax and smallBz+emitdz*z>zmin:
					#print(smallBx,smallBx+emitdx*x, smallBy+emitdy*y, smallBz+emitdz*z)
					
					if dist0(x,y,z)==1:
						S1.append([x,y,z])
						continue
				
					if dist0(x,y,z)==2:
						S2.append([x,y,z])
						continue
			
					if dist0(x,y,z)==3:
						S3.append([x,y,z])
	
	#print(S1, S2, S3)
	#print("=========")		
	for i in range(len(S1)):
		S1[i][0] = S1[i][0]*dx + delx
		S1[i][1] = S1[i][1]*dy + dely
		S1[i][2] = S1[i][2]*dz + delz
		
	for i in range(len(S2)):
		S2[i][0] = S2[i][0]*dx + delz
		S2[i][1] = S2[i][1]*dy + dely
		S2[i][2] = S2[i][2]*dz + delz
		
	for i in range(len(S3)):
		S3[i][0] = S3[i][0]*dx + delx
		S3[i][1] = S3[i][1]*dy + dely
		S3[i][2] = S3[i][2]*dz + delz
	
	#print(S1, S2, S3)
	'''
	
		
	S1 =([delx + dx, dely, delz],
		[delx - dx, dely, delz], 
		[delx, dely + dy, delz],
		[delx, dely - dy, delz],
		[delx, dely, delz + dz],
		[delx, dely, delz - dz])
		
	
	S2 =[
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
		]

	S3= [
		[delx + dx, dely + dy, delz + dz],
		[delx - dx, dely + dy, delz + dz],
		[delx - dx, dely - dy, delz + dz],
		[delx - dx, dely - dy, delz - dz],
		[delx + dx, dely - dy, delz - dz],
		[delx + dx, dely + dy, delz - dz],
		[delx + dx, dely + dy, delz + dz],
		[delx - dx, dely + dy, delz - dz]
		]
	
	'''print('---')
	print (S1)
	print('---')
	
	
	for i in range(len(S1)-1, -1, -1):
		if(emitter.ifSmallBlockExists(ox, oy, oz)==0):
			del(S1[i])
	
	for i in range(len(S2)-1, -1, -1):
		if(emitter.ifSmallBlockExists(ox, oy, oz)==0):
			del(S2[i])
	
	for i in range(len(S3)-1, -1, -1):
		if(emitter.ifSmallBlockExists(S3[i][0], S3[i][1], S3[i][2])==0):
			del(S3[i])
	
	'''
	return S1, S2, S3


#S1, S2, S3 are vectors of elements needed for sums, function calculates matrix factor
def calculateNxx(delx, dely, delz, dx, dy, dz, emitter, i):
	sum1 = 0.0
	sum2 = 0.0
	sum3 = 0.0
	S1, S2, S3 = generateSVectors(delx, dely, delz, dx, dy, dz, emitter, i)
	
	#print(S1, S2, S3)
	for vect in S1:
		sum1 = sum1 + f(vect[0], vect[1], vect[2])
		#print(sum1)
	
	for vect in S2:
		sum2 = sum2 + f(vect[0], vect[1], vect[2])
		
	for vect in S3:
		sum3 = sum3 + f(vect[0], vect[1], vect[2])
	
	#print(delx, dely, delz, dx,dy,dz, S1, S2, S3, "f", f(delx,dely,delz))
	return (1/(4.0*mt.pi*dx*dy*dz))*(8*f(delx, dely, delz)-(4*sum1) + 2*sum2 - sum3) #TU JEST LIPA Z JAKIEGOS POWODU
	#return (1/(4*mt.pi*delx*dely*delz))*(8*f(delx, dely, delz)-4*sum1 + 2*sum2 - sum3)

def calculateNxy(delx, dely, delz, dx, dy, dz, emitter, i):
	sum1 = 0
	sum2 = 0
	sum3 = 0
	
	S1, S2, S3 = generateSVectors(delx, dely, delz, dx, dy, dz, emitter, i)
	
	for vect in S1:
		sum1 = sum1 + g(vect[0], vect[1], vect[2])
	
	for vect in S2:
		sum2 = sum2 + g(vect[0], vect[1], vect[2])
		
	for vect in S3:
		sum3 = sum3 + g(vect[0], vect[1], vect[2])
	
	return (1/(4*mt.pi*dx*dy*dz))*(8*g(delx, dely, delz)-4*sum1 + 2*sum2 - sum3)
	
