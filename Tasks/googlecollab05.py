# Problem 1 FizzBuzz:
# Write a program that prints the numbers from 1 to 100. But for multiples of three, 
# print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".

def FizzBuzz():
    for i in range(1, 101):                 # We set our reading from 1 to 100
        if i % 3 == 0 and i % 5 == 0:       # to find which number is multiple of both 3 and 5, then print FizzBuzz
            print("FizzBuzz")
        elif i % 3 == 0:                    # to find number with multiple of 3, then print Fizz
            print("Fizz")
        elif i % 5 == 0:                    # to find number with multiple of 5, then print Buzz
            print("Buzz")
        else:
            print(i)                        # print numbers that arent included in multiple of both 3 and 5

FizzBuzz()                                  # Run the Function by calling it outside of its own function     
                                            

# Problem 2 Collatz Sequence:

# Write a program that takes an integer input from the user and generates the Collatz sequence for that number. 
# The Collatz sequence is defined as follows:
# start with a number n. If n is even, the next number is n/2. If n is odd, the next number is 3n + 1. 
# Repeat the process until n becomes 1.

def collatz_sequence(n):                                  # We set the function here by adding a parameter of n
    sequence = []                                         # Then we use an empty List to be fill by n later
    while n != 1:                                         # This is a way of use to set the limit to 1 when using While Loop
        if n % 2 == 0:                                    # To find even number only
            n = n // 2  
        else:                                             # To find the Odd only
            n = 3 * n + 1                           
        sequence.append(n)                                # Then we append the result of the calculation into the List, by writing it outside of the if else statement  
    return sequence                                       # this means the sequence will be the output of the function so we return it

user_input = int(input("Give a number: "))                # Simply just an input
sequence = collatz_sequence(user_input)                   # we declare that the sequence is the output of the function
print("This is your Collatz Sequence:", sequence)         # So that  we can print the result List


# Problem 3 GCD Calculation:

# Write a program that takes two integers from the user and 
# calculates their greatest common divisor (GCD) using the Euclidean algorithm.

def GCD_Calculation(a,b):                              # The function takes two parameters, a and b.
    c = a                                              # Inside the function, two variables c and d are assigned the values of a and b, respectively.
    d = b

    if c < d:                                          # The code checks if c is less than d. If true,
        c, d = d, c                                    # it swaps the values of c and d using tuple unpacking (c, d = d, c).

    while d != 0:                                      # The code enters a while loop that continues until d becomes 0.
        c, d = d, c % d                                # Inside the while loop, c and d are updated using the Euclidean algorithm: c is assigned the value of d, and d is assigned the remainder of c divided by d (d = c % d).
    return c                                           # Once d becomes 0, the while loop exits, and the function returns the value of c, which is the GCD of a and b.
      
a = int(input("Give your 1st number: "))               # The function is then called with user input for a and b
b = int(input("Give your 2nd number: "))               
print(f"\nGCD({a},{b}) = {GCD_Calculation(a,b)}\n")    # the calculated GCD is printed.



# Problem 4 Rock, Paper, Scissors:

# Write a program that plays the game of Rock, Paper, Scissors with the user. 
# The user makes a choice, the program randomly chooses, and the winner is determined.

import random                                                       # Import the random module to generate random numbers.

def get_player_choice():                                            # Here we start define the function
    print("\n1. Rock")                                              # function that prints the available choices 
    print("2. Paper")
    print("3. Scissors\n")

    choice = input("Choose wisely (1, 2, or 3): ")                  # prompts the player to enter their choice
    while choice not in ['1', '2', '3']:                            # It validates the input to ensure it's a valid choice (1, 2, or 3)
        print("Invalid choice! Please choose 1, 2, or 3.")
        choice = input("Choose wisely (1, 2, or 3): ")    
    
    return int(choice)                                              # returns the player's choice as an integer.

def get_computer_choice():                                          # We write another function for computer side
    return random.randint(1, 3)                                     # function that generates a random integer between 1 and 3 to represent the computer's choice.

def determine_winner(player_choice, computer_choice):               # Define the determine_winner() function that takes the player's and computer's choices as arguments
    choices = {1: "Rock",
               2: "Paper",
               3: "Scissors"}

    print(f"\nYou chose: {choices[player_choice]}")                 # prints the choice selected from player
    print(f"Computer chose: {choices[computer_choice]}")            # prints the choice selected from computer

    if player_choice == computer_choice:                            # determines the winner based on the rules of the game.
        return "It's a tie!"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return "You win!"                                           # It returns a string indicating the result.
    else:
        return "You lose!"                                          # It returns a string indicating the result.

while True:                                                         # Set up the main game loop using a while True loop. Infinite Loop if you didn't put break
    player_choice = get_player_choice()                             # Inside the loop, call the get_player_choice() to get the player's choice 
    computer_choice = get_computer_choice()                         # and get_computer_choice() functions to get the computer's choices.
    result = determine_winner(player_choice, computer_choice)       # Call the determine_winner() function to get the result.
    print(result)
    
    play_again = input("\nDo you want to play again? (y/n): ")      # Prompt the player to enter "y" to play again or any other key to quit.
    if play_again != "y":                                           # If the player enters "y", continue the loop.
        break                                                       # otherwise, break the loop.


# Problem 5 Number Guessing Game:

# Write a program that randomly generates a number between 1 and 100. 
# The user has to guess the number. After each guess, the program tells the user whether the guess is too high,
# too low, or correct. The game continues until the user guesses the correct number.

import random                                        # The random module is imported to generate random numbers.

def number_guessing_game():                          # The number_guessing_game() function is defined, which will contain the game logic.
    target_number = random.randint(1, 100)           # Inside the function, a random number between 1 and 100 is generated using random.randint(1, 100) and stored in the target_number variable.
    guessed_correctly = False                        # The guessed_correctly variable is initialized as False to keep track of whether the user has guessed the correct number.

    print("\nWelcome to the Number Guessing Game!")  # A welcome message and instructions are printed to the console.
    print("Guess the number I picked. \n")

    while not guessed_correctly:                                                              # A while loop is used to repeatedly prompt the user for a guess until the correct number is guessed.
        user_guess = input("Enter your guess: ")
        user_guess = int(user_guess)                                                          # The input is converted to an integer using int(user_guess).
        if user_guess < target_number:                                                        # If the user's guess is less than the target number, a message indicating that the guess is too low is printed.
            print("Your guess is too low. Try again!")
        elif user_guess > target_number:                                                      # If the user's guess is greater than the target number, a message indicating that the guess is too high is printed.
            print("Your guess is too high. Try again!")
        else:                                                                                 # If the user's guess is equal to the target number
            print(f"Congratulations! You guessed the correct number: {target_number}")        # a congratulatory message is printed,
            guessed_correctly = True                                                          # the guessed_correctly variable is set to True to exit the loop.

number_guessing_game()                                                                        # Finally, the function is called to start the game.


#Problem 6 Perfect Number: Write a program that generates 10 perfect numbers.

# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes

def is_perfect_number(n):                       # function takes an integer n as input and checks if it is a perfect number.
    divisors_sum = 1  
    for i in range(2, int(n**0.5) + 1):         # It calculates the sum of all divisors of n (excluding n itself) and checks if the sum equals n. 
        if n % i == 0:
            divisors_sum += i
        if i != n // i:                         # If they are equal, the function returns True
                divisors_sum += n // i
    return divisors_sum == n

def find_perfect(count):                        # function takes an integer count as input and finds the first count perfect numbers.
    perfect = []                                # It initializes an empty list perfect 
    num = 2                                     # a variable num with the value 2.
    while len(perfect) < count:                 # enters a while loop that continues until the length of perfect is equal to count. 
        if is_perfect_number(num):              # it checks if num is a perfect number using the is_perfect_number function.
            perfect.append(num)                 # If it is, num is appended to the perfect list.
        num += 1                                # incremented by 1 and the loop continues. 
    return perfect                              # Once the loop completes, the function returns the perfect list.

perfect = find_perfect(4)                       # In the main part of the code, the find_perfect function is called with the argument 4.
print(f"The 4 perfect number are: {perfect}")   # The resulting list of perfect numbers is stored in the perfect variable, and it is then printed using a formatted string.


#Problem 7 Harmonic Series:

# Write a program that calculates the sum of the first n terms of the harmonic series. Take the n as Input.

def series_sum(n):                                 # The function series_sum takes an integer n as input.
    sum = 0.0                                      # It initializes a variable sum to 0.0 to store the sum of the series.
    for i in range(1, n + 1):                      # It uses a for loop to iterate from 1 to n (inclusive) using the range function.
        sum += 1 / i                               # Inside the loop, it adds the reciprocal of the current iteration value (1 / i) to the sum variable.
    return sum                                     # After the loop finishes, it returns the calculated sum.

n = int(input("Enter the number of terms n: "))                                            # The main part of the code prompts the user to enter the number of terms n.
sum_of_harmonic = series_sum(n)                                                            # It calls the series_sum function with the user-provided n and stores the result in the variable sum_of_harmonic.
print(f"The sum of the first {n} terms of the harmonic series is: {sum_of_harmonic:.2f}")  # Finally, it prints the sum of the harmonic series with 2 decimal places using an f-string.


# Problem 8 Number to Words:

# Write a program that converts a number to its word representation (e.g., 123 to "one hundred twenty-three").

def number_to_words(num):                                                                 # The function number_to_words takes an integer num as input.
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']   # It initializes arrays ones, teens, and tens to store the English word representations 
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    def convert_to_words(n):                  # function that takes an integer n as input and returns its English word 
        if n < 10:                            # It checks if n is less than 10
            return ones[n]
        elif n < 20:                          # between 10 and 19
            return teens[n - 10]
        else:
            return tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10])            # greater than or equal to 20.

    if num == 0:                                # it checks if the input number is 0 and returns 'zero' 
        return 'zero'

    words = ''                                  # It initializes an empty string words to store the English word representation of the input number.
    if num >= 100:                              # If the input number is greater than or equal to 100
        words += ones[num // 100] + ' hundred'  # removes the hundreds place from num, and appends 'hundred' to words. 
        num %= 100                              # If there is still a remaining number after removing the hundreds place
        if num > 0:
            words += ' and '                    # it appends ' and ' to words.

    if num > 0:                                 # If there is a remaining number after handling the hundreds place,
        words += convert_to_words(num)          # it appends the English word representation of the remaining number to words using the convert_to_words function.

    return words.strip()                        # Finally, it returns the words string after removing any leading or trailing whitespace.

num = int(input("Enter a number: "))
print(f"{num} in words is:", number_to_words(num))


# Problem 9 Roman to Integer

# Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral

def roman_to_integer(s):                                    # function takes a Roman numeral as input and converts it to an integer.
    roman_map = {                                           # The roman_to_integer function takes a Roman numeral as input and converts it to an integer.
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,         # It uses a dictionary (roman_map) to map Roman numerals to their corresponding integer values.
        'D': 500, 'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in s:                               # The function iterates through the Roman numeral
        current_value = roman_map[char] 
        result += current_value                  # adding the corresponding integer value to the result.
        if current_value > prev_value:           # If the current value is greater than the previous value
            result -= 2 * prev_value             # it subtracts twice the previous value from the result to handle subtractive notation
        prev_value = current_value
    
    return result

def integer_to_roman(num):                       # function takes an integer as input and converts it to a Roman numeral
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),   # It uses a list of tuples (roman_map) to map integer values to their corresponding Roman numeral symbols.
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""                                  # It initializes an empty string words to store
    
    for value, symbol in roman_map:              # The function iterates through the list
        while num >= value:                      # appending the corresponding Roman numeral symbol to the result as long as the integer is greater than or equal to the value.
            result += symbol
            num -= value
    
    return result

while True:                                      # The program then enters a loop that displays a menu to the user
    print("\nChoose an option:")
    print("1. Convert integer to Roman numeral")
    print("2. Convert Roman numeral to integer")
    
    choice = input("\nEnter your choice (1/2): ")
    
    if choice == '1':
        num = int(input("\nEnter an integer: "))
        print(f"{num} in Roman numeral is: {integer_to_roman(num)}\n")
        break
    elif choice == '2':
        roman_numeral = input("\nEnter a Roman numeral: ")
        print(f"{roman_numeral} in integer is: {roman_to_integer(roman_numeral)}\n")
        break
    else:                                               
        print("Invalid choice. Please enter 1 or 2.")      # user enters an invalid choice, an error message is displayed.


# Problem 10 String Compression

# Write a program to perform basic string compression using the counts of repeated characters 
# (e.g., "aabcccccaaa" -> "a2b1c5a3").

def compress_string(s):                                 # defines a function called compress_string that takes a string s as input and compresses it using a simple algorithm
    compressed = ""                                     # The function initializes an empty string compressed to store the compressed string
    count = 1                                           # an integer count to keep track of consecutive occurrences
    prev_char = s[0]                                    # a variable prev_char to store the previous character encountered.
    
    for i in range(1, len(s)):                          # The function iterates through the input string s starting from the second character (index 1) using a for loop.
        if s[i] == prev_char:                           # Inside the loop, it checks if the current character s[i] is equal to the previous character prev_char. 
            count += 1                                  # If they are equal, it increments the count by 1.
        else:
            compressed += prev_char + str(count)        # If the current character is not equal to the previous character, 
            prev_char = s[i]                            # it appends the previous character and its count to the compressed string.
            count = 1                                   # Then, it updates prev_char with the current character and resets count to 1.
    
    compressed += prev_char + str(count)                # After the loop finishes, it appends the last character and its count to the compressed string.    
    return compressed                                   # Finally, the function returns the compressed string.

input_str = "aabcccccaaa"
compressed_str = compress_string(input_str)
print(f'\nOriginal string: {input_str}')
print(f'\nCompressed string: {compressed_str}\n')
