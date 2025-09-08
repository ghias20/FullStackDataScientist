import random
import string
a=int(input("Enter length of password : "))
b=random.choices(string.ascii_letters + string.digits + "@",k=a)
password=''.join((b))
print(password)