import math
class Shape:
    def __init__(self,name):
        self.name=name

    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius=radius

    def area(self):
        return round(math.pi*self.radius**2,2)
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
c=Circle(7)
r=Rectangle(4,5)
print(c.area())
print(r.area())
