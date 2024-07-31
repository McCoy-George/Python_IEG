# I-Design 1

#1
def pirint():
    return("\nWelcome to Amphi Event Management System\n")

print(pirint())

#2
def reg(cust_name):
    return f"\nHello {cust_name} ! Welcome  to Amphi Event Management System\n"

print("Enter you name: ")
cust_name = input()
print(reg(cust_name))

# 3
def Total_Expenses_for_the_Event():
    x = branding + travel + food + logistics

    branding_percentage = (branding / x) * 100
    travel_percentage = (travel / x) * 100
    food_percentage = (food / x) * 100
    logistics_percentage = (logistics / x) * 100

    result = (
        f"\nTotal expenses : Rs.{x:.2f}\n"
        f"Branding expenses percentage : {branding_percentage:.2f}%\n"
        f"Travel expenses percentage : {travel_percentage:.2f}%\n"
        f"Food expenses percentage : {food_percentage:.2f}%\n"
        f"Logistics expenses percentage : {logistics_percentage:.2f}%\n"
    )
    return result

print("Enter branding expenses")
branding = int(input())

print("Enter travel expenses")
travel = int(input())

print("Enter food expenses")
food = int(input())

print("Enter logistics expenses")
logistics = int(input())

print(Total_Expenses_for_the_Event())

# 4
def Tickets_sold_for_Charity_Event(X,Y):
    c = (Y - 5 * X) / 13
    c = int(c)

    a = c + X
    s = 2 * c
    
    return c,a,s
    
print("Enter the value of X")
X = int(input())

print("Enter the value of Y")
Y = int(input())

c, a, s = Tickets_sold_for_Charity_Event(X,Y)

print(f"Number of children tickets sold : {c}")
print(f"Number of adult tickets sold : {a}")
print(f"Number of senior tickets sold : {s}")

# 5
def Tile_Game(side_length,num_tiles):
    k = int((num_tiles ** 0.5))
    largest_square_side = k * side_length
    largest_square_area = largest_square_side ** 2

    return f"Area of the largest possible square is {largest_square_area}sqcm"

print("Enter the side in cm of a square tile")
side_length = int(input())

print("Enter the number of square tiles available")
num_tiles = int(input())

print(Tile_Game(side_length,num_tiles))

# 6
def Amos(total_salary):
    E = (total_salary - 800) / 130
    W = E + 10

    result = (
        f"Number of weekday hours is {int(W)}\n"
        f"Number of weekend hours is {int(E)}"
    )
    return result
    
print("Enter the total salary paid")
total_salary = float(input())

print(Amos(total_salary))

# I-asses (WonderWorks Magic Show)
def WonderWorks_Magic_Show():
    total_people = A + B + C

    weighted_sum = (A * A1 + B * B1 + C * C1)

    overall_average_rating = weighted_sum / total_people
    
    return overall_average_rating
    
A = int(input("Enter the number of people who watched show 1\n"))
A1 = float(input("Enter the average rating for show 1\n"))

B = int(input("Enter the number of people who watched show 2\n"))
B1 = float(input("Enter the average rating for show 2\n"))

C = int(input("Enter the number of people who watched show 3\n"))
C1 = float(input("Enter the average rating for show 3\n"))

overall_average_rating = WonderWorks_Magic_Show()
print(f"The overall average rating for the show is {overall_average_rating:.2f}")


# I-Design 2

#1
def Lucky_Winner(ticket_number):
    last_digit = ticket_number % 10

    if last_digit == 3 or last_digit == 8:
        return "Lucky Winner"
    else:
        return "Not a Lucky Winner"

ticket_number = int(input())
print(Lucky_Winner(ticket_number))

#2
def Ticket_Types(ticket):
    if ticket == 'E' or ticket == 'e':
        return "Early Bird Ticket"
    elif ticket == 'D' or ticket == 'd':
        return "Discount Ticket"
    elif ticket == 'V' or ticket == 'v':
        return "VIP Ticket"
    elif ticket == 'S' or ticket == 's':
        return "Standard Ticket"
    elif ticket == 'C' or ticket == 'c':
        return "Child Ticket"
    else:
        return "Invalid ticket type"
    
ticket = input()
print(Ticket_Types(ticket))

#3
def Total_Expenses(ticket_cost, num_tickets):
    total_cost = ticket_cost * num_tickets

    if num_tickets < 50:
        Expenses = total_cost
    elif num_tickets <= 100:
        Expenses = total_cost * 0.9  
    elif num_tickets <= 200:
        Expenses = total_cost * 0.8  
    elif num_tickets <= 400:
        Expenses = total_cost * 0.7  
    elif num_tickets <= 500:
        Expenses = total_cost * 0.6  
    else:
        Expenses = total_cost * 0.5  
    return Expenses
    
ticket_cost = float(input())
num_tickets = int(input())

Expenses = Total_Expenses(ticket_cost, num_tickets)
print(f"{Expenses:.2f}")

#4
def Salary_Computation(Danny_salary):
    if (Danny_salary < 15000):
        HRA =  Danny_salary*0.15    
        DA = Danny_salary*0.9
    elif (Danny_salary >= 15000):
        HRA =  5000    
        DA = Danny_salary*0.98
        
    Gross = float(Danny_salary + HRA + DA)
    return Gross
    
Danny_salary = int(input())
print(f"{Salary_Computation(Danny_salary):.2f}")

#5
def Grades_of_Rides(hurl_factor, spin_factor,speed_factor):
    if hurl_factor > 50 and spin_factor > 60 and speed_factor > 100:
        grade = 10
    elif hurl_factor > 50 and spin_factor > 60:
        grade = 9
    elif spin_factor > 60 and speed_factor > 100:
        grade = 8
    elif hurl_factor > 50 and speed_factor > 100:
        grade = 7
    elif hurl_factor > 50 or spin_factor > 60 or speed_factor > 100:
        grade = 6
    else:
        grade = 5
    return grade
    
factors = input().strip().split()
hurl_factor = int(factors[0])
spin_factor = int(factors[1])
speed_factor = int(factors[2])

print(Grades_of_Rides(hurl_factor, spin_factor,speed_factor))

#I-asses
def Card_Game(card1_type, card1_number, card2_type, card2_number,card3_type, card3_number):   
    if (card1_type == card2_type == card3_type) and (card1_number == card2_number == card3_number):
        return "Double Bonanza"
    elif (card1_type == card2_type == card3_type) or (card1_number == card2_number == card3_number):
        return "Bonanza"
    else:
        return "No Bonanza"
        
card1_type, card1_number = input().split()
card2_type, card2_number = input().split()
card3_type, card3_number = input().split()

card1_number = int(card1_number)
card2_number = int(card2_number)
card3_number = int(card3_number)

print(Card_Game(card1_type, card1_number, card2_type, card2_number,card3_type, card3_number))

# Lab 5, question 2
# Function to generate the Collatz sequence
def collatz_sequence(n):
    sequence = [n]  # Start with the initial number
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Use integer division
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Get user input
user_input = int(input("Give a number: "))

# Generate the Collatz sequence
sequence = collatz_sequence(user_input)

# Print the sequence in the desired format
print("This is your Collatz Sequence:", ",".join(map(str, sequence)))
