# Problem 1

# Write a python function that takes a number as parameter and prints the multiplication table of that number

def mult_table(num):                                    # Define a function called mult_table that takes an integer num as input
    result = []                                         # Initialize an empty list called result to store the multiplication table lines
    for i in range(1, 13):                              # Loop over the range from 1 to 13 (exclusive)
        result.append(f"{num} x {i} = {num * i}")       # Append a formatted string to the result list representing a multiplication table line  
    return result                                       # Return the result list containing the multiplication table lines

table = mult_table(5)                                   # Call the mult_table function with the argument 5 and store the result in the variable table
for line in table:                                      # Loop over each line in the table list
    print(line)                                         # Print each line


# Problem 2

# Write a simple python function that returns twin primes less than 1000.
# If two consecutive odd numbers are both prime then they are known as twin primes.


def is_prime(n):                                  # Function to check if a number is prime
    if n <= 1:                                    # If the number is less than or equal to 1, it is not prime
        return False
    if n <= 3:                                    # If the number is less than or equal to 3, it is prime
        return True
    if n % 2 == 0 or n % 3 == 0:                  # If the number is divisible by 2 or 3, it is not prime
        return False
    i = 5                                         # Start checking from 5
    while i * i <= n:                             # Continue checking until the square of i is greater than n
        if n % i == 0 or n % (i + 2) == 0:        # If the number is divisible by i or i+2, it is not prime
            return False
        i += 6                                    # Increment i by 6 (to check only odd numbers)
    return True                                   # If no factors are found, the number is prime

def twin_primes(limit):                           # Function to find twin primes up to a given limit
    twin_primes = []                              # Initialize an empty list to store the twin prime pairs
    for num in range(3, limit, 2):                # A for loop is used to iterate through odd numbers starting from 3 up to the given limit, with a step of 2. This is done to skip even numbers, as they cannot be prime.
        if is_prime(num) and is_prime(num + 2):   # Check if both num and num+2 are prime
            twin_primes.append((num, num + 2))    # If they are, append a tuple (num, num+2) to the twin_primes list
    return twin_primes                            # Return the list of twin prime pairs

primes_list = twin_primes(1000)                   # Find twin primes up to 1000

for line in primes_list:                          # Print each twin prime pair
    print(line)


# Problem 3

# Write a simple python function that takes a number as parameter and returns the prime factors of that number.
# Prime Factorization is finding which prime numbers multiply together to make the original number.


def prime_factors(n):           # Define a function to find prime factors of a number

    i = 2                       # Start with the smallest prime number
    factors = []                # Initialize an empty list to store the prime factors
    while i * i <= n:           # Loop until the square of the current number is less than or equal to the input number
        if n % i:               # If the input number is not divisible by the current number, increment the current number
            i += 1
        else:
            n //= i             # If the input number is divisible by the current number, divide it and add the current number to the list of factors
            factors.append(i)
    if n > 1:                   # If the remaining number is greater than 1, it is a prime factor itself
        factors.append(n)
    return factors              # Return the list of prime factors
print(prime_factors(63))        # Print the prime factors of 63


# Problem 4

# Write a function that inputs a number and returns the product of digits of that number.


def product_of_digits(n):             # Function to calculate the product of digits of a number

    product = 1                       # Initialize product to 1
    while n > 0:                      # Loop until n becomes 0
        digit = n % 10                # Extract the last digit of n
        product *= digit              # Multiply the product with the last digit
        n //= 10                      # Remove the last digit from n
    return product                    # Return the product

print(product_of_digits(123))         # Test the function with the number 123


# Problem 5

# Write a function that takes a number as parameter. The function finds the proper divisors of that number
# and then finds the sum of proper divisors. Proper divisors of a number are those numbers by
# which the number is divisible, except the number itself.


def proper_divisors_list(n):             # Function to calculate the list of proper divisors of a number
    proper_divisors = []                 # Initialize an empty list to store the proper divisors
    for i in range(1, n):                # Loop through numbers from 1 to n-1
        if n % i == 0:                   # If the current number is a divisor of n
            proper_divisors.append(i)    # Add the divisor to the list of proper divisors
    return proper_divisors               # Return the list of proper divisors

print(proper_divisors_list(36))          # Test the function with the number 36


# Problem 6

# A number is called perfect if the sum of proper divisors of that number is equal to the number.
# For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range


def get_proper_divisors(n):                   # Function to get all proper divisors of a number
    divisors = [1]                            # Initialize divisors with 1
    for i in range(2, int(n**0.5) + 1):       # Loop through numbers up to square root of n
        if n % i == 0:                        # If i is a divisor
            divisors.append(i)                # Add i to divisors
            if i != n // i:                   # If i is not equal to n divided by i (to avoid duplicates)
                divisors.append(n // i)       # Add n divided by i to divisors
    return divisors

def is_perfect_number(n):                     # Function to check if a number is perfect
    return sum(get_proper_divisors(n)) == n   # Check if sum of proper divisors is equal to n

def print_perfect_numbers_in_range(limit):                       # Function to print all perfect numbers in a given range
    for num in range(2, limit + 1):                              # Loop through numbers in the given range
        if is_perfect_number(num):                               # If number is perfect
            divisors = get_proper_divisors(num)                  # Get proper divisors
            print(f"{' + '.join(map(str, divisors))} = {num}")   # Print proper divisors and number

print_perfect_numbers_in_range(100)                            # Call function with limit 10000





# Problem 7

# Write a python function that takes 2 parameters lower and upper (range). 
# Let the function returns pairs of amicable numbers in that range.
# Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number. 


def amicable_numbers(lower, upper):                          # Define a function to find amicable numbers within a given range
    def sum_of_divisors(n):                                  # Define a helper function to calculate the sum of proper divisors of a number
        divisors = [i for i in range(1, n) if n % i == 0]    # List comprehension to find divisors
        return sum(divisors)                                 # Return the sum of divisors

    amicable_pairs = []                                         # Initialize an empty list to store amicable pairs
    for num in range(lower, upper):                             # Iterate over each number in the given range
        sum_num = sum_of_divisors(num)                          # Calculate the sum of proper divisors of the current number
        if sum_num > num and sum_of_divisors(sum_num) == num:
        # Check if the sum of proper divisors of the current number is greater than the current number
        # and if the sum of proper divisors of the sum of proper divisors is equal to the current number
            amicable_pairs.append((num, sum_num))               # Append the current number and its pair to the amicable pairs list

    return amicable_pairs                                       # Return the list of amicable pairs

print(amicable_numbers(1, 1000))                                # Call the function with the range 1 to 1000 and print the result


# Problem 8

# Write a python function that takes variable length parameters and returns maximum and minimum number in the parameter numbers.


def maximumMinimum(*numbers):        # Function to find the maximum and minimum numbers in a variable length parameter list
    maximum = numbers[0]             # Initialize maximum and minimum with the first number
    minimum = numbers[0]

    for num in numbers[1:]:          # Iterate over the rest of the numbers
        if num > maximum:            # Update maximum if current number is greater
            maximum = num
        elif num < minimum:          # Update minimum if current number is smaller
            minimum = num
    return [minimum, maximum]        # Return a list containing the minimum and maximum numbers

print(maximumMinimum(10, 20, 30, 40, 50))


# Problem 9

# Write a simple Python function that takes a number(n) as a parameter. Then the function prints out
# the first n rows of Pascal's triangle. Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.


def print_pascal_triangle(n):
    row = [1]                                                 # Initialize the first row
    for i in range(n):
        spaces = " " * (n - i - 1)                            # Calculate the number of spaces before the first number
        print(spaces + " ".join(str(num) for num in row))     # Print the spaces and the row
        next_row = [1]                                        # Generate the next row
        
        for j in range(len(row) - 1):                         # Iterate over the indices of the current row (excluding the last index)
            next_row.append(row[j] + row[j + 1])              # Add the sum of adjacent elements in the current row to the next row
        next_row.append(1)                                    # Add the last element (always 1) to the next row
        row = next_row                                        # Update the current row with the next row

print_pascal_triangle(10)


# Problem 10

# Write a simple python function that accepts a hyphen-separated sequence of words as parameter and
# returns the words in a hyphen-separated sequence after sorting them alphabetically.


def sort_hyphenated_words(words):                    # Function to sort hyphenated words in a given string
    word_list = words.split('-')                     # Split the string into a list of words using '-' as the delimiter  
    
    for i in range(len(word_list)):                  # Implement bubble sort to sort the list of words
        for j in range(i + 1, len(word_list)):
            if word_list[i] > word_list[j]:                                # Swap words if the current word is greater than the next word
                word_list[i], word_list[j] = word_list[j], word_list[i] 
                
    sorted_sequence = '-'.join(word_list)                                  # Join the sorted list of words back into a string using '-' as the delimiter   
    return sorted_sequence                                                 # Return the sorted string

sample_items = "green-red-yellow-black-white-ayam-zebra"
result = sort_hyphenated_words(sample_items)                               # Call the function with the sample input and store the result
print("Expected Result:", result)                                          # Print the expected result
