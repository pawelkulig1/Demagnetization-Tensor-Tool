class test: 
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def ifInEllipse(self, x, y):
		if (x**2/self.a**2) + (y**2/self.b**2) <= 1:
			return True
		else:
			return False
			
			

elipsa1 = test(2,3)
print(elipsa1.ifInEllipse(1,1))
