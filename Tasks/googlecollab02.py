#Exercise 1: Check Even or Odd
x = int(input("Enter your number: "))

if (x % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

# Exercise 2: Grade Evaluation
mark = int(input("Enter your grade: "))

if (mark >= 90 and mark <=100):
    print("Your Grade is A, Outstanding work!")
elif (mark >= 80 and mark <= 89):
    print("Your Grade is B, Great job!")
elif (mark >= 70 and mark <= 79):
    print("Your Grade is C, Good effort! I can see you trying")
elif (mark >= 60 and mark <= 69):
    print("Your Grade is D, Needs improvement!")
elif (mark < 60):
    print("Your Grade is F, Let's work harder!")
else:
    print("Please try again")

#Exercise 3: Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Exercise 4: Number Comparison
first = int(input("Enter 1st number: "))
second = int(input("Enter 2nd number: "))
third = int(input("Enter 3rd number: "))

if (first > second and first > third):
    print(first, "is the largest number")
elif (second > first and second > third):
    print(second, "is the largest number")
elif (third > first and third >second):
    print(third, "is the largest number")
else:
    print("All numbers are equal")

# Exercise 5: Check Vowel or Consonant
vowels = {'a', 'e', 'i', 'o', 'u'}
consonant = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}

character = str(input("Enter a letter: "))

if (character in vowels):
    print(character, "is a vowel")
elif (character in consonant):
    print(character, "is a consonant") 

# #Exercise 6: BMI Calculator
weight = float(input("Enter the weight (kg): "))
height = float(input("Enter the height (meters): "))
BMI = weight/(height**2)

if (BMI < 18.5):
    print("Your BMI is", round(BMI, 2), "Which is Underweight")
elif (BMI >= 18.5 and BMI < 24.9):
    print("Your BMI is", round(BMI, 2), "Which is Normal weight")
elif (BMI >= 25 and BMI < 29.9):
    print("Your BMI is", round(BMI, 2), "Which is Overweight")
elif (BMI >= 30):
    print("Your BMI is", round(BMI, 2), "Which is Obesity")
else:
    print("Please try again")

#Exercise 7: Triangle Type Checker
first_side = float(input("Enter 1st side: "))
second_side = float(input("Enter 2nd side: "))
third_side = float(input("Enter 3rd side: "))

if (first_side == second_side) and (first_side == third_side):
    print("Equilateral triangle")
elif (first_side == second_side) and (first_side != third_side):
    print("Isosceles triangle")
elif (first_side != second_side) and (first_side != third_side) and (second_side != third_side):
    print("Scalene triangle")
else:
    print("Please try again")

# Exercise 8: ATM Withdrawal
dollar = int(input("Enter your amount: $"))
print("Your amount is: $", dollar)

if dollar >= 50:
    print(dollar // 50, "x $50")
    dollar %= 50
if dollar >= 20:
    print(dollar // 20, "x $20")
    dollar %= 20
if dollar >= 10:
    print(dollar // 10, "x $10")
    dollar %= 10
if dollar >= 1:
    print(dollar // 1, "x $1")
else:
    print("There is something wrong with your input.")

#Exercise 9: Adam Number
number = int(input("Enter a number: "))

ori_square = number**2
print("Original number after square:", ori_square)

if number <= 999 and number > 99:
    num = number
    a = num // 100
    num %= 100
    b = num // 10
    num %= 10
    c = num
    swapped_num = c * 100 + b * 10 + a 
    print("Swapped number: ", swapped_num)
    swap_square = swapped_num**2
    print("Swapped number after square:", swap_square)
    number_str  = str(ori_square) 
    reversed_str  = number_str [4] + number_str [3]+ number_str [2] + number_str [1] + number_str [0]
    reversed_square = int(reversed_str )
    
if number <= 99 and number > 9: 
    num = number
    a = num // 10
    num %= 10
    b = num
    swapped_num =b * 10 + a 
    print("Swapped number: ", swapped_num)
    swap_square = swapped_num**2
    print("Swapped number after square:", swap_square)
    number_str  = str(ori_square) 
    reversed_str  = number_str [2] + number_str [1] + number_str [0]
    reversed_square = int(reversed_str )

    
if (swap_square == reversed_square ):
    print( number, " is an Adam number")
else: 
    print( number, " is not an Adam number")



# Exercise 10: Armstrong Number
num = int(input("Enter a number: "))

if num <= 999 and num > 99:
    n = 3
    number = num
    a = number // 100
    number %= 100
    b = number // 10
    number %= 10
    c = number
    armstrong = a**n + b**n + c**n
    print("After Calculation:", armstrong)
    
elif num <= 99 and num > 9: 
    n = 2
    number = num
    d = number // 10
    number %= 10
    e = number
    armstrong = d**n + e**n
    print("After Calculation:", armstrong)

elif num <= 9:
    n = 1
    number = num
    f = number % 10
    armstrong = f**n
    print("After Calculation:", armstrong)
    
if (num == armstrong ):
    print( num, " is an Armstrong num")
elif (num != armstrong):
    print( num, " is not an Armstrong num")


