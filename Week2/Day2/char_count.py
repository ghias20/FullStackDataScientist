a=input("Enter a string : ")
d={}
for char in a:
    if char in d:
        d[char]+=1
    else:
        d[char]=1
print(d)