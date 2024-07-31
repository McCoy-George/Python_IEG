# Problem 1:
def is_pangram(sentence):
    sentence = sentence.lower()  
    letters_found = set()
    
    for char in sentence:
        if 'a' <= char <= 'z' and char not in letters_found:
            letters_found.add(char)      
        if len(letters_found) == 26:
            return True
    
    return len(letters_found) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog."))  


# Problem 2
def is_isogram(input_string):
    seen_letters = set()   
    for char in input_string:
        if char == ' ' or char == '-':    # Ignore spaces and hyphens
            continue      
        char_lower = char.lower()         
        if char_lower in seen_letters:  
            return False       
        seen_letters.add(char_lower)     
    return True  

user_input = input("Enter a string to check if it's an isogram: ")
print(is_isogram(user_input))


# Problem 3
def evaluate_word_problem(problem):
    # Define the mapping of words to operations
    def add(x, y): return x + y
    def sub(x, y): return x - y
    def mul(x, y): return x * y
    def div(x, y): return x // y

    operations = {
        'plus': add,
        'minus': sub,
        'multiplied by': mul,
        'divided by': div
    }

    # Remove the initial phrase "What is " and the trailing "?"
    problem = problem[8:-1]

    # Tokenize the problem by splitting the words
    tokens = problem.split()
    
    # Initialize the result with the first number
    result = int(tokens.pop(0))
    
    # Process the tokens in pairs of (operation, number)
    while tokens:
        # Get the operation
        operation = tokens.pop(0)
        if operation == 'multiplied' or operation == 'divided':
            operation += ' ' + tokens.pop(0)  # Combine with the next word for "multiplied by" or "divided by"
        
        # Get the number
        number = int(tokens.pop(0))
        
        # Apply the operation to the current result and the next number
        result = operations[operation](result, number)
    
    return result

# Test cases
print(evaluate_word_problem("What is 5?"))                        # 5
print(evaluate_word_problem("What is 5 plus 13?"))                # 18
print(evaluate_word_problem("What is 7 minus 5?"))                # 2
print(evaluate_word_problem("What is 6 multiplied by 4?"))        # 24
print(evaluate_word_problem("What is 25 divided by 5?"))          # 5
print(evaluate_word_problem("What is 5 plus 13 plus 6?"))         # 24
print(evaluate_word_problem("What is 3 plus 2 multiplied by 3?")) # 15


# Problem 4
def resistor_value(colors):
    color_to_value = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }
    
    # Split the colors input by "-"
    color_list = colors.split('-')
    
    # Get the values of the first two colors
    first_value = color_to_value[color_list[0].lower()]
    second_value = color_to_value[color_list[1].lower()]
    
    # Combine the values to form a two-digit number
    result = first_value * 10 + second_value
    
    return result

# Test cases
print(resistor_value("brown-green"))          # Should return 15
print(resistor_value("brown-green-violet"))   # Should return 15
print(resistor_value("red-blue"))             # Should return 26
print(resistor_value("yellow-grey"))          # Should return 48


# Problem 5
def validate_credit_card(card_number):
    # Remove spaces from the card number and reverse it
    card_number = card_number.replace(' ', '')[::-1]
    
    total_sum = 0
    for i in range(len(card_number)):
        digit = int(card_number[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
    
    return total_sum % 10 == 0

# Test case
card_number = "4539 3195 0343 6467"
print(validate_credit_card(card_number))  # Should return True


# Problem 6
class StringProcessor:
    def __init__(self):
        self.input_string = ""
    
    def getString(self):
        self.input_string = input("Enter a string: ")
    
    def printString(self):
        print("Uppercase String:", self.input_string.upper())

# Example usage:
processor = StringProcessor()
processor.getString()  # Prompts the user to enter a string
processor.printString()  # Prints the entered string in uppercase


# Problem 7
class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.id = emp_id
        self.name = name
        self.salary = salary
        self.department = department
    
    def calculateSalary(self, hours_worked):
        base_salary = self.salary
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = overtime_hours * (base_salary / 50)
            total_salary = base_salary + overtime_amount
        else:
            total_salary = base_salary
        
        return total_salary
    
    def assignDepartment(self, new_department):
        self.department = new_department
    
    def __str__(self):
        return f"\nID: {self.id}, Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

# Sample Employee Data
employees = [
    Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
    Employee("E7499", "JONES", 45000, "RESEARCH"),
    Employee("E7900", "MARTIN", 50000, "SALES"),
    Employee("E7698", "SMITH", 55000, "OPERATIONS")
]

# Example usage:
for emp in employees:
    print(emp)  # Printing employee details using __str__ method
    print("Initial Salary for 40 hours:", emp.calculateSalary(40))  # Calculate salary for 40 hours
    emp.assignDepartment("HR")  # Assign new department
    print("New Department:", emp.department)  # Print updated department
    print("Salary for 60 hours:", emp.calculateSalary(60))  # Calculate salary for 60 hours including overtime
    print()  # Print empty line for separation


# Problem 8
class Inventory:
    def __init__(self):
        self.inventory_data = {}
    
    def addItem(self, item_id, product_name, available_quantity, price):
        self.inventory_data[item_id] = {
            "name": product_name,
            "availableQuantity": available_quantity,
            "price": price
        }
        print(f"Item added successfully: ID {item_id}, Name: {product_name}, Quantity: {available_quantity}, Price: {price}")
    
    def updateItem(self, item_id, product_name=None, available_quantity=None, price=None):
        if item_id in self.inventory_data:
            if product_name is not None:
                self.inventory_data[item_id]["name"] = product_name
            if available_quantity is not None:
                self.inventory_data[item_id]["availableQuantity"] = available_quantity
            if price is not None:
                self.inventory_data[item_id]["price"] = price
            print(f"Item updated successfully: ID {item_id}")
        else:
            print(f"Item with ID {item_id} not found in inventory")
    
    def checkItem_details(self, item_id):
        if item_id in self.inventory_data:
            item_details = self.inventory_data[item_id]
            print(f"Item ID: {item_id}")
            print(f"Name: {item_details['name']}")
            print(f"Available Quantity: {item_details['availableQuantity']}")
            print(f"Price: ${item_details['price']:.2f}")
        else:
            print(f"Item with ID {item_id} not found in inventory")

# Sample Data
sample_inventory_data = {
    "97410": {
        "name": "Television",
        "availableQuantity": 20,
        "price": 1455.99
    },
    "97411": {
        "name": "Radio",
        "availableQuantity": 32,
        "price": 654.25
    }
}

# Example usage:
inventory = Inventory()

# Add items from sample data
for item_id, item_details in sample_inventory_data.items():
    inventory.addItem(item_id, item_details["name"], item_details["availableQuantity"], item_details["price"])

# Update an item
inventory.updateItem("97411", product_name="Portable Radio", price=700.50)

# Check item details
inventory.checkItem_details("97410")
inventory.checkItem_details("97411")
inventory.checkItem_details("97412")  # Item not present


# Problem 9
class BankAccount:
    def __init__(self, account_number, opening_balance, customer_name, date_of_opening):
        self.accountNumber = account_number
        self.openingBalance = opening_balance
        self.currentBalance = opening_balance
        self.customerName = customer_name
        self.dateOfOpening = date_of_opening
    
    def deposit(self, amount):
        self.currentBalance += amount
        print(f"\nDeposited ${amount:.2f} successfully.")
    
    def withdraw(self, amount):
        if self.currentBalance >= amount:
            self.currentBalance -= amount
            print(f"\nWithdrawn ${amount:.2f} successfully.")
        else:
            print("\nInsufficient funds.")
    
    def checkBalance(self):
        print(f"\nCurrent Balance: ${self.currentBalance:.2f}")

# Example usage:
account = BankAccount("123456789", 1000.00, "John Doe", "2024-07-10")

account.checkBalance()  # Check initial balance

account.deposit(500.50)  # Deposit money
account.checkBalance()

account.withdraw(200.75)  # Withdraw money
account.checkBalance()

account.withdraw(2000.00)  # Attempt to withdraw more than available
account.checkBalance()


# Problem 10
def validate_brackets(s):                              # Function to validate if brackets in a string are properly nested and closed

    stack = []                                         # Initialize an empty stack to keep track of opening brackets

    mapping = {')': '(', ']': '[', '}': '{'}           # Define a mapping of closing brackets to their corresponding opening brackets

    
    for char in s:                                     # Iterate over each character in the string

        if char in mapping:                            # If the character is a closing bracket

            if stack and stack[-1] == mapping[char]:   # Check if the stack is not empty and the last opening bracket matches the closing bracket

                stack.pop()                # If it does, remove the opening bracket from the stack

            else:
                return False               # If it doesn't, return False as the brackets are not properly nested or closed

        elif char in mapping.values():     # If the character is an opening bracket

            stack.append(char)             # Add the opening bracket to the stack

    
    return len(stack) == 0                 # If the stack is empty after iterating over all characters, return True as all brackets are properly nested and closed


# Define a list of test cases
test_cases = [
    "()",      
    "()[]{}", 
    "[)",     
    "({[)]",   
    "{{{",     
]

for case in test_cases:                  # Iterate over each test case
    if validate_brackets(case):          # If the brackets in the test case are properly nested and closed, print "valid"
        print(f'"{case}" is valid')
    else:                                # If the brackets in the test case are not properly nested or closed, print "invalid"
        print(f'"{case}" is invalid')