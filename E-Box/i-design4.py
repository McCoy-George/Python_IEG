# 1
def salute(name, message="Welcome to Python Programming"):
       print(f"Hello {name}, {message}")

print("Menu")
print("1. Name and Message")
print("2. Name")

choice = int(input())

if choice == 1:
    print("Enter the name")
    name = input()
    print("Enter the message")
    message = input()
    salute(name, message)
elif choice == 2:
    print("Enter the name")
    name = input()
    salute(name)
else:
    print("Invalid choice")

# 2
def daysInYear(year, check_leap=True):

    if check_leap:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")


year = int(input())
daysInYear(year)

# 3
def GCD(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    print(f"Greatest common divisor of {original_n1} and {original_n2} = {n1}")

def LCM(n1, n2):
    gcd = n1
    while n2:
        gcd, n2 = n2, gcd % n2
    lcm = original_n1 * original_n2 // gcd
    print(f"Least common multiple of {original_n1} and {original_n2} = {lcm}")

print("Enter two integers:")
n1 = int(input())
n2 = int(input())

original_n1 = n1
original_n2 = n2

GCD(n1, n2)
LCM(n1, n2)

# 4
def addition(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")

def subtraction(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")

def multiplication(n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")

def division(n1, n2):
    if n2 != 0:
        print(f"{n1} / {n2} = {n1 / n2}")
    else:
        print("Error: Division by zero")

def modulus(n1, n2):
    if n2 != 0:
        print(f"{n1} % {n2} = {n1 % n2}")
    else:
        print("Error: Modulus by zero")

print("Select the operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")

print("Enter the choice(1/2/3/4/5):")
choice = int(input())

if choice == 1:
    print("Enter the first number")
    n1 = int(input())
    print("Enter the second number")
    n2 = int(input())
    addition(n1, n2)
elif choice == 2:
    print("Enter the first number")
    n1 = int(input())
    print("Enter the second number")
    n2 = int(input())
    subtraction(n1, n2)
elif choice == 3:
    print("Enter the first number")
    n1 = int(input())
    print("Enter the second number")
    n2 = int(input())
    multiplication(n1, n2)
elif choice == 4:
    print("Enter the first number")
    n1 = int(input())
    print("Enter the second number")
    n2 = int(input())
    division(n1, n2)
elif choice == 5:
    print("Enter the first number")
    n1 = int(input())
    print("Enter the second number")
    n2 = int(input())
    modulus(n1, n2)
else:
    print("Invalid Input")

# 5
def div_thirteen(n, arr):
    if n <= 0:
        print("Invalid input")
    else:
        found_divisible = False
        
        
        is_divisible_by_thirteen = lambda x: x % 13 == 0
        
        
        for num in arr:
            if is_divisible_by_thirteen(num):
                if found_divisible:
                    print(" ", end="")  
                print(num, end="")  
                found_divisible = True
        
        if found_divisible:
            print()  
        else:
            print("")  

print("Enter size of list")
n = int(input())

if n <= 0:
    print("Invalid input")
else:
    print("Enter the elements in list")
    arr = []
    for i in range(n):
        arr.append(int(input()))
    
    div_thirteen(n, arr)

# I-asses
def multiply(argument1, argument2=10):
    result = argument1 * argument2
    return result

a = int(input())
b = int(input())

result1 = multiply(a)
result2 = multiply(a, b)
result3 = multiply(a, 9)

print(f"The result is {result1}")
print(f"The result is {result2}")
print(f"The result is {result3}")
