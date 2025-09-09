defaulters={}
for _ in range(5):
    name=input("Enter name: ")
    attendance=int(input("ENter attendance : "))
    if (attendance<75):
        defaulters[name]=attendance
print(defaulters)