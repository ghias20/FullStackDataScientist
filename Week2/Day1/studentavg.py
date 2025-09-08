class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_average(self):
        return sum(self.marks)/len(self.marks)
    def add_mark(self,mark):
        self.marks.append(mark)
    def get_highest(self):
        return max(self.marks)
    def get_lowest(self):
        return min(self.marks)
s=Student("Tom",[90,80,85])
print(s.get_average())
s.add_mark(95)
print(s.get_highest())
