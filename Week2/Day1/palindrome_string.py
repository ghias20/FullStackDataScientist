a=input("Enter a string : ")
def palindrome_string(a):
    a=a.lower()
    a=a.replace(" ","")
    b=a[::-1]
    if a==b:
        return True
    return False
print(palindrome_string(a))