def f(x):
    return eval(equation)  

def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return None 
    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    
    return (a + b) / 2 


equation = input("Enter the equation in terms of x : ")
a = float(input("Enter the starting point of the interval (a): "))
b = float(input("Enter the ending point of the interval (b): "))
tolerance = float(input("Enter the tolerance : "))
root = bisection_method(a, b, tol=tolerance)

if root is not None:
    print(f"Root found: {root}")
else:
    print("No root found in interval.")
