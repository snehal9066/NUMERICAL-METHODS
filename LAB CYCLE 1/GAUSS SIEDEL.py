def gaussseidel(a, x ,b):
	n = len(a)				 
	for j in range(0, n):	 
		d = b[j]				 
		for i in range(0, n):	 
			if(j != i):
				d-=a[j][i] * x[i] 
		x[j] = d / a[j][j]	 
	return x 

n = 3							
a = []						 
b = []	 
#enter diagonally dominant matrix				 
x = [0, 0, 0]					 
a = [[9, 1, 5],[8, 10, 9],[2, -7, -10]]
b = [14,7,-23]
print(x)

#loop run for m times depending on m the error value
for i in range(0, 10):		 
	x = gaussseidel(a, x, b)
	print("Value of x at iteration-",i,"are: ",x)
