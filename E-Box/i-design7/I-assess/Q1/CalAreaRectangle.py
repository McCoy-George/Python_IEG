from Shape import Shape

class CalAreaRectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.breadth}")
        print(f"Area of Rectangle : {self.length * self.breadth}")
