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
	

	#overloading addition returns delta(x), delta(y), delta(z)
	def __add__(self, other):
		return (self.xpoz-other.xpoz), (self.ypoz-other.ypoz), (self.zpoz-other.zpoz)
	

def radius(x,y,z):
	return mt.sqrt(x**2 + y**2 + z**2)

def wspolczynnik (delx,dely,delz, x,y,z, emitter):
    xx = abs(x-delx)/(emitter.widthSmall)
    yy = abs(y-dely)/(emitter.heightSmall)
    zz = abs(z-delz)/(emitter.depthSmall)

    if int(xx+yy+zz+0.5)==0:
        return 8.0
    if int(xx+yy+zz+0.5)==1:
        return -4.0
    if int(xx+yy+zz+0.5)==2:
        return 2.0
    else:
        return -1.0

def f(x,y,z):
	R = radius(x, y, z)
	
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

def generateSVectors(delx, dely, delz, dx, dy, dz):
	'''S1 =([delx + dx, dely, delz],
		[delx - dx, dely, delz], 
		[delx, dely + dy, delz],
		[delx, dely - dy, delz],
		[delx, dely, delz + dz],
		[delx, dely, delz - dz])
		
	
	S2 =(
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
		)

	S3= (
		[delx + dx, dely + dy, delz + dz],
		[delx - dx, dely + dy, delz + dz],
		[delx - dx, dely - dy, delz + dz],
		[delx - dx, dely - dy, delz - dz],
		[delx + dx, dely - dy, delz - dz],
		[delx + dx, dely + dy, delz - dz],
		[delx + dx, dely - dy, delz + dz],
		[delx - dx, dely + dy, delz - dz]
		)'''
	
	'''S = ([delx + dx, dely, delz],
		[delx - dx, dely, delz], 
		[delx, dely + dy, delz],
		[delx, dely - dy, delz],
		[delx, dely, delz + dz],
		[delx, dely, delz - dz],
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
		[delx - dx, dely, delz - dz],
		[delx + dx, dely + dy, delz + dz],
		[delx - dx, dely + dy, delz + dz],
		[delx - dx, dely - dy, delz + dz],
		[delx - dx, dely - dy, delz - dz],
		[delx + dx, dely - dy, delz - dz],
		[delx + dx, dely + dy, delz - dz],
		[delx + dx, dely - dy, delz + dz],
		[delx - dx, dely + dy, delz - dz]
		)'''
		
		
		
    
    
    
	return S

def calculateNxx(delx, dely, delz, dx, dy, dz, emitter):
    xran = [delx-dx, delx, delx+dx]
    yran = [dely-dy, dely, dely+dy]
    zran = [delz-dz, delz, delz+dz]

    Nxx = 0
	
    for x in xran:
        for y in yran:
            for z in zran:
                Nxx += wspolczynnik(delx, dely, delz, x,y,z, emitter)*f(x,y,z)

    
    return Nxx

def calculateNxy(delx, dely, delz, dx, dy, dz, emitter):
    xran = [delx-dx, delx, delx+dx]
    yran = [dely-dy, dely, dely+dy]
    zran = [delz-dz, delz, delz+dz]

    Nxy = 0

    for x in xran:
        for y in yran:
            for z in zran:
                Nxy += wspolczynnik(delx, dely, delz, x,y,z, emitter)*g(x,y,z)
    
    return Nxy
	
