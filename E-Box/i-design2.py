# 1
ticket_number = int(input())

last_digit = ticket_number % 10

if last_digit == 3 or last_digit == 8:
    print("Lucky Winner")
else:
    print("Not a Lucky Winner")

# 2
ticket = input()

if ticket == 'E' or ticket == 'e':
    print("Early Bird Ticket")
elif ticket == 'D' or ticket == 'd':
    print("Discount Ticket")
elif ticket == 'V' or ticket == 'v':
    print("VIP Ticket")
elif ticket == 'S' or ticket == 's':
    print("Standard Ticket")
elif ticket == 'C' or ticket == 'c':
    print("Child Ticket")
else:
    print("Invalid ticket type") 

# 3
ticket_cost = float(input())
num_tickets = int(input())

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

print(f"{Expenses:.2f}")

# 4
Danny_salary = int(input())

if (Danny_salary < 15000):
    HRA =  Danny_salary*0.15    
    DA = Danny_salary*0.9
elif (Danny_salary >= 15000):
    HRA =  5000    
    DA = Danny_salary*0.98
    
Gross = float(Danny_salary + HRA + DA)
print(f"{Gross:.2f}")

# 5
factors = input().strip().split()
hurl_factor = int(factors[0])
spin_factor = int(factors[1])
speed_factor = int(factors[2])

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

print(grade)

# I-asses
card1_type, card1_number = input().split()
card2_type, card2_number = input().split()
card3_type, card3_number = input().split()

card1_number = int(card1_number)
card2_number = int(card2_number)
card3_number = int(card3_number)

if (card1_type == card2_type == card3_type) and (card1_number == card2_number == card3_number):
    print("Double Bonanza")
elif (card1_type == card2_type == card3_type) or (card1_number == card2_number == card3_number):
    print("Bonanza")
else:
    print("No Bonanza")

