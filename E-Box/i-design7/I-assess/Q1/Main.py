from CalAreaSquare import CalAreaSquare
from CalAreaRectangle import CalAreaRectangle
from CalAreaTriangle import CalAreaTriangle
from CalAreaCircle import CalAreaCircle

print("Select an Option")
print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")
choice = int(input())

if choice == 1:
    side = int(input("Enter the side\n"))
    shape = CalAreaSquare(side)
elif choice == 2:
    length = int(input("Enter the length\n"))
    breadth = int(input("Enter the breadth\n"))
    shape = CalAreaRectangle(length, breadth)
elif choice == 3:
    base = int(input("Enter the base\n"))
    height = int(input("Enter the height\n"))
    shape = CalAreaTriangle(base, height)
elif choice == 4:
    radius = int(input("Enter the radius\n"))
    shape = CalAreaCircle(radius)
else:
    print("Invalid choice")
    shape = None

if shape:
    shape.area()
