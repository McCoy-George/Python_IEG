from Shape import Shape

class CalAreaTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
        print(f"Area of Triangle : {0.5 * self.base * self.height:.2f}")
