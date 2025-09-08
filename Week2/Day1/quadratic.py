import math
def quadratic_solver(a, b, c):
    discriminant=b**2-4*a*c
    if discriminant<0:
        return "No real roots"
    elif discriminant==0:
        root=-b/(2*a)
        return f"Root is: {root}"
    else:
        root1=(-b+math.sqrt(discriminant))/(2*a)
        root2=(-b-math.sqrt(discriminant))/(2*a)
        return f"Roots are: {root1} and {root2}"
print(quadratic_solver(1, -3, 2))
