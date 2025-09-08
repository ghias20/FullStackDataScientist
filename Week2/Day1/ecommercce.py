class Order:
    def __init__(self):
        self.items={}
    def add(self,item,price):
        self.items[item]=price
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    def calculate_total(self):
        return f"Total = {sum(self.items.values())}"
    def show_items(self):
        print(self.items)
order=Order()
order.add("Shirt",500)
order.add("Shoes",1500)
print(order.calculate_total())
