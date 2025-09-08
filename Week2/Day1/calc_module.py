import math
opt=int(input("ENter option 1.sqrt 2.factorial 3.sin 4.cos : "))
a=int(input("Enter a number to perform operation : "))
if (opt==1):
    print( math.sqrt(a))
if (opt==2):
    print( math.factorial(a))
if (opt==3):
    print( math.sin(a))
if (opt==4):
    print( math.cos(a))
