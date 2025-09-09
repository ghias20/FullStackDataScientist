a=int(input("Enter 1st value : "))
b=int(input("Enter 2nd value : "))
op=int(input("Enter 1.add 2.sub 3.mul 4.div : "))
if op==1:
    c=a+b
    print("Sum is : ",c)
elif op==2:
    c=a-b
    print("Difference is : ",c)
elif op==3:
    c=a*b
    print("Mul is : ",c)
elif op==4:
    c=a/b
    print("Div is : ",c)