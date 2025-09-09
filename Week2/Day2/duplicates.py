a=input("Enter Students names : ").split()
dupl=[]
for name in range(0,len(a)):
    for j in range(name+1,len(a)):
        if(a[name]==a[j]):
            dupl.append(a[name])
print(dupl)