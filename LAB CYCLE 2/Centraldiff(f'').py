import math
def f(x):
    return math.sin(x)
def CDD(x,h):
    centraldiff=(f(x+h)+f(x-h)-(2*f(x)))/(h**2)
    return centraldiff
h=float(input("Enter the step size here:"))
x=math.pi/4

f=CDD(x,h)
print("The Second Derivative of Central Divided Difference value is: ",f)