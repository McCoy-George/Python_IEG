# Exercise 1: Basic Arithmetic Operations

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
print( "Addition of x and y: ", x + y )
print( "Subtraction of x and y: ", x - y )
print( "Multiplication of x and y: ", x * y )
print( "Division of x and y: ", x / y )

# Exercise 2: Temperature Converter
C = float(input("Enter the Celsius value:"))
F = (C * 9/5) + 32
print("The temprature in Fahrenheit is: ", F)

# Exercise 3: Area and Perimeter of a Rectangle
x = float(input("Enter the length:"))
y = float(input("Enter the width:"))
parameter = 2*x + 2*y
area = x*y
print("The area and parameter of the rectangle are:", area, "&", parameter, "respectively")

# Exercise 4: Simple Interest Calculator
P = float(input("Enter the principal amount:"))
R = float(input("Enter the rate of interest:"))
T = int(input("Enter the time in years:"))
RR = R / 100 #since it has percentage
SI = P * RR * T
print("The simple interest is: ", SI)

# Exercise 5: Swapping Two Variables
x = input("Enter the first number: ")
y = input("Enter the second number: ")
print("Before swapping: x =",x, "&","y =",y)
z = x
x = y
y = z
print("After swapping: x =",x ,"&","y =",y)

# Exercise 6: Square and Cube
x = int(input("Enter the first number: "))

Square = x **2
Cube = x **3
print("The Square :", Square)
print("The Cube :", Cube)

# Exercise 7: Calculate BMI
weight = float(input("Enter the weight (kg): "))
height = float(input("Enter the height (meters): "))
BMI = weight/(height**2)
print("The BMI is:", round(BMI, 2))

# Exercise 8: Compound Interest Calculator
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
t = int(input("Enter the time in years: "))
n = float(input("Enter times interest is compounded per year: "))

A = P * (1 + R / (100 * n)) ** (n * t)

print("Thecompound interest is", round(A, 2))

# Exercise 9: Convert 97409 to Binary
number = 97409
a0 = number % 2 
b0 = number // 2 

a1 = b0 % 2
b1 = b0 // 2 

a2 = b1 % 2
b2 = b1 // 2 

a3 = b2 % 2
b3 = b2 // 2 

a4 = b3 % 2
b4 = b3 // 2 

a5 = b4 % 2
b5 = b4 // 2 

a6 = b5 % 2
b6 = b5 // 2 

a7 = b6 % 2
b7 = b6 // 2 

a8 = b7 % 2
b8 = b7 // 2 

a9 = b8 % 2
b9 = b8 // 2 

a10 = b9 % 2
b10 = b9 // 2 

a11 = b10 % 2
b11 = b10 // 2 

a12 = b11 % 2
b12 = b11 // 2 

a13 = b12 % 2
b13 = b12 // 2 

a14 = b13 % 2
b14 = b13 // 2 

a15 = b14 % 2
b15 = b14 // 2 

a16 = b15 % 2
b16 = b15 // 2 

bin= str(a16) + str(a15) + str(a14) + str(a13) + str(a12) + str(a11) + str(a10) + str(a9) + str(a8) + str(a7) + str(a6) + str(a5) + str(a4) + str(a3) + str(a2) + str(a1) + str(a0)

print("Binary representation of", number, "is:", bin)

# Exercise 10: Convert 1011 to Decimal
binary = "1011"
decimal = (1 * (2 ** 3)) + (0 * (2 ** 2)) + (1 * (2 ** 1)) + (1 * (2 ** 0))

print("Decimal representation of", binary, "is:", decimal)
