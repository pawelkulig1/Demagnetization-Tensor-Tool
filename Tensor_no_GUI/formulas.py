import mpmath as mp

class Block:
    def __init__(self, width, depth, height, xpoz, ypoz, zpoz, wElements, dElements, hElements):
        self.smallBlocksStructure = []
        self.xpoz = mp.mpmathify(xpoz)
        self.ypoz = mp.mpmathify(ypoz)
        self.zpoz = mp.mpmathify(zpoz)

        self.width = mp.mpmathify(width)
        self.depth = mp.mpmathify(depth)
        self.height = mp.mpmathify(height)

        self.wElements = mp.mpmathify(mp.nint(wElements))
        self.dElements = mp.mpmathify(mp.nint(dElements))
        self.hElements = mp.mpmathify(mp.nint(hElements))

        self.widthSmall = mp.mpmathify(self.width / self.wElements)
        self.depthSmall = mp.mpmathify(self.depth / self.dElements)
        self.heightSmall = mp.mpmathify(self.height / self.hElements)
        self.nElements = mp.nint((self.width * self.depth * self.height) / (self.widthSmall * self.depthSmall * self.heightSmall))

    def isInStructure(self, xpoint, ypoint, zpoint):
        return True

    def createStructure(self):
        startw = (self.widthSmall / 2) + self.xpoz
        startd = (self.depthSmall / 2) + self.ypoz
        starth = (self.heightSmall / 2) + self.zpoz

        #print(startw, starth, startd, self.widthSmall, self.depthSmall, self.heightSmall)
        #print(self.width, self.depth, self.height)
        #print(self.wElements, self.dElements, self.hElements)

        for i in mp.arange(self.wElements):
            for j in mp.arange(self.dElements):
                for k in mp.arange(self.hElements):
                    if self.isInStructure(startw+self.widthSmall*i, startd+self.depthSmall*j, starth+self.heightSmall*k):
                        self.smallBlocksStructure.append([startw+self.widthSmall*i, startd+self.depthSmall*j, starth+self.heightSmall*k])
        self.nElements = mp.mpmathify(len(self.smallBlocksStructure))

class Rectangle(Block):
    def __init__(self, width, depth, height, xpoz, ypoz, zpoz, wElements, dElements, hElements):
        super(Rectangle, self).__init__(width, depth, height, xpoz, ypoz, zpoz, wElements, dElements, hElements)

    # all objects from rectangle are inside of rectangular shape
    def isInStructure(self, xpoint, ypoint, zpoint):
        return True


class Ellipse(Block):
    def __init__(self, a, b, height, axis, xpoz, ypoz, zpoz, wElements, dElements, hElements):
        # axis is 0 for x,y; 1 for y,z; and 2 for x,z
        self.axis = axis
        #if self.axis == 0:
        super(Ellipse, self).__init__(a, b, height, xpoz, ypoz, zpoz, wElements, dElements, hElements)

    def isInStructure(self, xpoint, ypoint, zpoint):
        if self.axis == 0:
            if (mp.power((xpoint - self.width - self.xpoz), 2) / mp.power(self.width, 2) + (mp.power((ypoint - self.depth- self.ypoz), 2) /mp.power(self.depth, 2)) <= 1 and zpoint <= self.zpoz + self.height and zpoint >= self.zpoz):
                return True


        elif self.axis == 1:
            if (mp.power((ypoint - self.depth - self.ypoz), 2) / mp.power(self.depth, 2)) + (mp.power((zpoint - self.height - self.zpoz), 2) / mp.power(self.height, 2)) <= 1 and xpoint <= self.xpoz + self.width and xpoint >= self.xpoz:
                return True

        else:
            if (mp.power((xpoint - self.width - self.xpoz), 2) / mp.power(self.width, 2)) + (mp.power((zpoint - self.height - self.zpoz), 2) / mp.power(self.height, 2)) <= 1 and ypoint <= self.ypoz + self.height and ypoint >= self.ypoz:
                return True

        return False


def radius(x, y, z):
    return mp.sqrt(mp.power(x, 2) + mp.power(y, 2) + mp.power(z, 2))

def wspolczynnik(delx, dely, delz, x, y, z, emitter):       
    counter = 0
    if delx == x:
        counter+=1
    if dely == y:
        counter+=1
    if delz == z:
        counter+=1
    
    if counter == 3:
        return 8.0
    elif counter == 2:
        return -4.0
    elif counter == 1:
        return 2.0
    else:
        return -1.0

def f(x, y, z):
    x = mp.mpmathify(x)
    y = mp.mpmathify(y)
    z = mp.mpmathify(z)
	
    R = radius(x, y, z)

    # solving 0 division problem here

    if x == 0 and z == 0 or y == 0:
        part1 = mp.mpmathify(0)
    else:
        part1 = mp.mpf('0.5') * y * (mp.power(z, 2) - mp.power(x, 2)) * mp.asinh(y / (mp.sqrt(mp.power(x, 2) + mp.power(z, 2))))

    if x == 0 and y == 0 or z == 0:
        part2 = 0
    else:
        part2 = mp.mpf('0.5') * z * (mp.power(y, 2) - mp.power(x, 2)) * mp.asinh(z / (mp.sqrt(mp.power(x, 2) + mp.power(y, 2))))

    if x == 0 or y == 0 or z == 0:
        part3 = 0
    else:
        part3 = x * y * z * mp.atan((y * z) / (x * R))

    # solving 0 division problem here

    part4 = mp.mpf('1 / 6') * R * (2 * mp.power(x, 2) - mp.power(y, 2) - mp.power(z, 2))

    return mp.mpmathify(part1 + part2 - part3 + part4)

def g(x, y, z):
    x = mp.mpmathify(x)
    y = mp.mpmathify(y)
    z = mp.mpmathify(z)

    R = radius(x, y, z)
	
    if x == 0 and y == 0:
        part1 = mp.mpf('0')
    else:
        part1 = x * y * z * mp.asinh(z / (mp.sqrt(mp.power(x, 2) + mp.power(y, 2))))

    if y == 0 and z == 0:
        part2 = mp.mpf('0')
    else:
        part2 = mp.mpf('1 / 6') * y * (3 * mp.power(z, 2) - mp.power(y, 2)) * mp.asinh(x / (mp.sqrt(mp.power(y, 2) + mp.power(z, 2))))

    if x == 0 and z == 0:
        part3 = 0
    else:
        part3 = mp.mpf('1 / 6') * x * (3 * mp.power(z, 2) - mp.power(x, 2)) * mp.asinh(y / (mp.sqrt(mp.power(x, 2) + mp.power(z, 2))))

    if y == 0:
        part4 = 0
    else:
        part4 = mp.mpf('0.5') * mp.power(y, 2) * z * mp.atan((x * z) / (y * R))

    if x == 0:
        part5 = 0
    else:
        part5 = mp.mpf('0.5') * mp.power(x, 2) * z * mp.atan((y * z) / (x * R))

    if z == 0:
        part6 = 0
    else:
        part6 = mp.mpf('1 / 6') * mp.power(z, 3) * mp.atan((x * y) / (z * R))

    part7 = mp.mpf('1 / 3') * x * y * R
    return part1 + part2 + part3 - part4 - part5 - part6 - part7



def calculateNxx(delx, dely, delz, dx, dy, dz, emitter, fLookUP):
    #mp.dps = 128
    #fLookUP = mp.memoize(f)
    
    xran = [delx - dx, delx, delx + dx]
    yran = [dely - dy, dely, dely + dy]
    zran = [delz - dz, delz, delz + dz]

    Nxx = 0

    for x in xran:
        for y in yran:
            for z in zran:
                Nxx += mp.mpmathify(wspolczynnik(delx, dely, delz, x, y, z, emitter) * fLookUP(x, y, z))
                #print(x,y,z,wspolczynnik(delx, dely, delz, x, y, z, emitter),  f(x, y, z), Nxx)
                #x
                #print(delx, dely, delz, dx, dy, dz)
    #print(Nxx)
    
    return Nxx

def calculateNxy(delx, dely, delz, dx, dy, dz, emitter, gLookUP):
    xran = [delx - dx, delx, delx + dx]
    yran = [dely - dy, dely, dely + dy]
    zran = [delz - dz, delz, delz + dz]
    #gLookUP = mp.memoize(g) 
    Nxy = 0

    for x in xran:
        for y in yran:
            for z in zran:
                Nxy += mp.mpmathify(wspolczynnik(delx, dely, delz, x, y, z, emitter) * gLookUP(x, y, z))
                #print(wspolczynnik(delx, dely, delz, x, y, z, emitter), gLookUP(x, y, z))
    
    #print("NXY : ", Nxy)
    
    return Nxy

def calculateDistance(cell1, cell2):
    return (mp.mpmathify(abs(cell1[0]-cell2[0])), mp.mpmathify(abs(cell1[1]-cell2[1])), mp.mpmathify(abs(cell1[2]-cell2[2])))
    
#fLookUP = mp.memoize(f)
#gLookUP = mp.memoize(g)    


