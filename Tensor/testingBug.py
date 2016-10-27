from formulas import *

print(calculateNxx(3.96e-8, 0,0,2e-10, 1e-09, 1e-09, [[3.94e-8, 0.0, 0.0]], [], []))
print(calculateNxx(3.98e-8, 0,0,2e-10, 1e-09, 1e-09, [[3.96e-8, 0.0, 0.0]], [], []))
print(calculateNxx(4.00e-8, 0,0,2e-10, 1e-09, 1e-09, [[3.98e-8, 0.0, 0.0]], [], []))
print("======================")
print(calculateNxx(2.5e-8, 0,0,2e-10, 1e-09, 1e-09, [[2.48e-8, 0.0, 0.0]], [], []))
print(calculateNxx(1.5e-8, 0,0,2e-10, 1e-09, 1e-09, [[1.48e-8, 0.0, 0.0]], [], []))
#przelomowy wniosek - czy tu nie powinno zamiast polozenia byc odleglosci czyli w S1 nie powinno byc zamiast delx-dx poprostu dx?

print(calculateNxx(0,0,0, 2e-10, 1e-09, 1e-09, [[0.02e-8, 0.0, 0.0]], [], []))
print(calculateNxx(0.02e-08,0,0, 2e-10, 1e-09, 1e-09, [[0, 0.0, 0.0]], [], []))


'''i=0
while(i<10e-08):
	print(i,";",f(i, 0, 0))
	i+=0.02e-08
	'''
