import math as mt

def radius(x,y,z):
	return mt.sqrt(x**2 + y**2 + z**2)
	
def f(x,y,z):
	R = radius(x, y, z)
	if x==0 or y==0 or z == 0:
		print("some error occured", x, y, z)
		exit()
	return (
		0.5*y*(z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
		+ 0.5*z*(y**2 - x**2) * mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		- x*y*z*((y*z)/(x*R))
		+ (1/6)*R*(2*x**2 - y**2 - z**2)
	)

def g(x,y,z):
	R = radius(x, y, z)
	
	return (
		x*y*z*mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		+ (1/6)*y*(3*z**2 - y**2) * mt.asinh(x/(mt.sqrt(y**2 + z**2)))
		+ (1/6)*x*(3*z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
		- 0.5*y**2*z * mt.atan((x*z)/(y*R))
		- 0.5*x**2*z * mt.atan((y*z)/(x*R))
		- (1/6)*z**3 * mt.atan((x*y)/(z*R))
		- (1/3)*x*y*R
	)

#S1, S2, S3 are vectors of elements needed for sums, function calculates matrix factor
def calculateNxx(delx, dely, delz, dx, dy, dz, S1, S2, S3):
	sum1 = 0
	sum2 = 0
	sum3 = 0
	
	for vect in S1:
		sum1 = sum1 + f(vect[0], vect[1], vect[2])
	
	for vect in S2:
		sum2 = sum2 + f(vect[0], vect[1], vect[2])
		
	for vect in S3:
		sum3 = sum3 + f(vect[0], vect[1], vect[2])
		
	return (1/(4*mt.pi*dx*dy*dz))*(8*f(delx, dely, delz)-4*sum1 + 2*sum2 - sum3)

def calculateNxy(delx, dely, delz, dx, dy, dz, S1, S2, S3):
	sum1 = 0
	sum2 = 0
	sum3 = 0
	
	for vect in S1:
		sum1 = sum1 + g(vect[0], vect[1], vect[2])
	
	for vect in S2:
		sum2 = sum2 + g(vect[0], vect[1], vect[2])
		
	for vect in S3:
		sum3 = sum3 + g(vect[0], vect[1], vect[2])
	
	return (1/(4*mt.pi*dx*dy*dz))*(8*g(delx, dely, delz)-4*sum1 + 2*sum2 - sum3)
	

#returns sum of f function with arguments from k vector	
def fsum(k):
	total = 0
	for i in k:
		total = total + f(i[0],i[1],i[2])
	print(total)
	
#returns sum of f function with arguments from k vector
def gsum(k):
	total = 0
	for i in k:
		total = total + g(i[0],i[1],i[2])
	print(total)
