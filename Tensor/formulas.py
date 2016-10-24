import math as mt

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
		
	if x==0 and z==0:
		part1=0
	else:
		part1 = 0.5*y*(z**2 - x**2) * mt.asinh(y/(mt.sqrt(x**2 + z**2)))
	
	if x==0 and y==0:
		part2=0
	else:
		part2 = 0.5*z*(y**2 - x**2) * mt.asinh(z/(mt.sqrt(x**2 + y**2)))
		
	if x==0:
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
