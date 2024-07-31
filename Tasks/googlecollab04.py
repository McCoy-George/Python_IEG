# Problem 1
counter = 1
while counter <= 10:
    print(counter, end=' ')
    counter += 1



# Problem2
prime_count = 0

for num in range(2, 30):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            # If num is not prime, set is_prime to False and stop checking further
            i = num  # This will exit the inner for loop
    
    if is_prime:
        print(num, end=' ')
        prime_count += 1
    
    # Check if we have found 10 prime numbers
    if prime_count == 10:
        num = 30  # This will exit the outer for loop



# Problem 3
# Prompt user for input
num_items = int(input("Enter number of Adam numbers to generate: "))

# Validate input
if num_items > 0:
    adam_numbers = []  # List to store Adam numbers
    count = 0  # Counter for Adam numbers found
    num = 0  # Start checking numbers from 0
    
    while count < num_items:
        # Calculate square of num and its reverse
        num_square = num ** 2
        num_reverse = int(str(num)[::-1])
        num_reverse_square = num_reverse ** 2
        
        # Check if they have reversed digits
        if str(num_square)[::-1] == str(num_reverse_square):
            adam_numbers.append(num)
            count += 1
        
        num += 1  # Move to the next number
    
    # Print the generated Adam numbers
    print(f"The first {num_items} Adam numbers are: {adam_numbers}")
else:
    print("Number of items must be a positive integer.")



# Problem 4
num_items = int(input("Enter number of Armstrong numbers to generate: "))

if num_items > 0:
    armstrong_numbers = []  
    count = 0  
    num = 100  
    
    while count < num_items:
        num_str = str(num)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        
        
        if sum_of_powers == num:
            armstrong_numbers.append(num)
            count += 1
        
        num += 1 
    
    print(f"The first {num_items} Armstrong numbers are: {armstrong_numbers}")
else:
    print("Number of items must be a positive integer.")

# Problem 5
num_rows = 5

for i in range(1, num_rows + 1):
    print('o' * i )



# Problem 6
num_rows = 5

for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Problem 7
n = int(input("Enter a number: "))

sum_of_numbers = 0

for i in range(1, n + 1):
    sum_of_numbers += i

print(f"The sum of all numbers from 1 to {n} is: {sum_of_numbers}")



# Problem 8
import sys

if len(sys.argv) < 2:
    print("Please provide some numbers as command line arguments.")
    sys.exit(1)

numbers = sys.argv[1:]

print("All elements:")
for num in numbers:
    print(num, end=' ')
print()  

print("Elements in even positions:")
for i in range(1, len(numbers), 2): 
    print(numbers[i], end=' ')
print()  

print("Elements in odd positions:")
for i in range(0, len(numbers), 2):  
    print(numbers[i], end=' ')
print() 



# Problem 9
import sys

if len(sys.argv) < 2:
    print("Please provide some numbers as command line arguments.")
    sys.exit(1)

numbers = sys.argv[1:]

numbers = [float(num) for num in numbers]

total_sum = sum(numbers)

average = total_sum / len(numbers)

print(f"The average of the given numbers is: {average:.2f}")



# Problem 10
input_string = input("Enter numbers separated by commas: ")

numbers_str = input_string.split(',')
numbers = [int(num) for num in numbers_str]

unique_numbers = set(numbers)

if len(unique_numbers) == len(numbers):
    print("\nAll the numbers are different from each other.")
else:
    print("There are duplicate numbers.")

print("\nThe list of numbers is:", numbers, "\n")


# Problem 11
input_string = input("Enter numbers separated by commas: ")

numbers_str = input_string.split(',')
numbers = [int(num) for num in numbers_str]

found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            num1 = numbers[i]
            num2 = numbers[j]
            num3 = numbers[k]
            if num1 + num2 + num3 == 100:
                print(f"Three numbers whose sum is 100: {num1}, {num2}, {num3}")
                found = True

if not found:
    print("No combination of three unique numbers whose sum is 100 found.")



# Problem 12
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

if num1 <= 0 or num2 <= 0:
    print("Both numbers must be positive integers.")
else:
    product = 0

    for i in range(num2):
        product += num1
    
    print(f"{num1} x {num2} = {product}")



# Problem 13
fibonacci_series = [0, 1]

while len(fibonacci_series) < 10:
    next_term = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_term)

print(f"\nThe first 10 terms of the Fibonacci series are: {fibonacci_series} \n")



# Problem 14
number = int(input("Enter a positive integer: "))

if number < 0:
    print("Please enter a positive integer.")
else:
    binary_representation = ''
    
    if number == 0:
        binary_representation = '0'
    else:
        while number > 0:
            remainder = number % 2
            binary_representation = str(remainder) + binary_representation
            number = number // 2

    print(f"The binary representation is: {binary_representation}")

# Problem 15
binary_input = input("Enter a binary number: ")
decimal_number = 0
binary_str = binary_input[::-1]

for i in range(len(binary_str)):  
    bit_value = int(binary_str[i])
    decimal_number += bit_value * (2 ** i)

print(f"The decimal representation of the binary number {binary_input} is {decimal_number}")
