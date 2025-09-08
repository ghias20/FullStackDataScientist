import sys
def sum_cl():
    if len(sys.argv) != 4:
        print("Usage: python add.py num1 num2 num3")
        return
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    num3=int(sys.argv[3])
    print("Sum =",num1+num2+num3)
sum_cl()
