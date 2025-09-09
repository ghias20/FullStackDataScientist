n=int(input("Enter total no of entries in a bill: "))
bill={}
for _ in range(n):
    item=input("ENter item name: ")
    price=int(input("Enter price of the item: "))
    bill[item]=price
print(sum(bill.values()))