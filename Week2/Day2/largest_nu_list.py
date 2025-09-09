a=list(map(int,input("ENter elements : ").split()))
largest=a[0]
for i in range(0,len(a)):
    if (a[i]>largest):
        largest=a[i]
print(largest)