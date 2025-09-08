def anagram(a,b):
    a=sorted(a)
    b=sorted(b)
    if(a==b):
        return True
    return False
a=input("enter word 1: ")
b=input("Enter word 2: ")
print(anagram(a,b))