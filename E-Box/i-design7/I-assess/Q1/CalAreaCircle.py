from Shape import Shape

class CalAreaCircle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Radius of Circle : {self.radius}")
        print(f"Area of Circle : {3.14 * self.radius ** 2:.2f}")
