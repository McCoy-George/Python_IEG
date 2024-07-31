from Shape import Shape

class CalAreaSquare(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print(f"Side of Square : {self.side}")
        print(f"Area of Square : {self.side ** 2}")
