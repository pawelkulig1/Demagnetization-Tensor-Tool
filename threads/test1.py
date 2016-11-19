def f1(x=[]):
	print(x[0])
	return x[0]

def f2(x=[]):
	print(x[0])
	x[0]=x[0]+1
	return x[0]

x = []
x.append(2)
f1(x)
f2(x)
f1(x)


