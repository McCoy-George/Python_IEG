# 1
print ("Welcome to Amphi Event Management System.")

# 2
print("Enter your name")
cust_name = input()  
print(f"Hello {cust_name} ! Welcome to Amphi Event Management System")

# 3
print("Enter branding expenses")
branding_expenses = int(input())

print("Enter travel expenses")
travel_expenses = int(input())

print("Enter food expenses")
food_expenses = int(input())

print("Enter logistics expenses")
logistics_expenses = int(input())

total_expenses = branding_expenses + travel_expenses + food_expenses + logistics_expenses

branding_percentage = (branding_expenses / total_expenses) * 100
travel_percentage = (travel_expenses / total_expenses) * 100
food_percentage = (food_expenses / total_expenses) * 100
logistics_percentage = (logistics_expenses / total_expenses) * 100

print(f"Total expenses : Rs.{total_expenses:.2f}")
print(f"Branding expenses percentage : {branding_percentage:.2f}%")
print(f"Travel expenses percentage : {travel_percentage:.2f}%")
print(f"Food expenses percentage : {food_percentage:.2f}%")
print(f"Logistics expenses percentage : {logistics_percentage:.2f}%")

# 4
print("Enter the value of X")
X = int(input())

print("Enter the value of Y")
Y = int(input())

c = (Y - 5 * X) / 13

c = int(c)

a = c + X
s = 2 * c

print(f"Number of children tickets sold : {c}")
print(f"Number of adult tickets sold : {a}")
print(f"Number of senior tickets sold : {s}")

# 5
print("Enter the side in cm of a square tile")
side_length = int(input())

print("Enter the number of square tiles available")
num_tiles = int(input())

k = int((num_tiles ** 0.5))

largest_square_side = k * side_length

largest_square_area = largest_square_side ** 2

print(f"Area of the largest possible square is {largest_square_area}sqcm")

# 6
print("Enter the total salary paid")
total_salary = float(input())

E = (total_salary - 800) / 130

W = E + 10

print(f"Number of weekday hours is {int(W)}")
print(f"Number of weekend hours is {int(E)}")


# 7
import sys

arguments = sys.argv[1:]
print("Arguments :")
for arg in arguments:
    print(arg)
print(f"Number of arguments is {len(arguments)}")

# I-asses
num_people_show1 = int(input("Enter the number of people who watched show 1\n"))
avg_rating_show1 = float(input("Enter the average rating for show 1\n"))

num_people_show2 = int(input("Enter the number of people who watched show 2\n"))
avg_rating_show2 = float(input("Enter the average rating for show 2\n"))

num_people_show3 = int(input("Enter the number of people who watched show 3\n"))
avg_rating_show3 = float(input("Enter the average rating for show 3\n"))

total_people = num_people_show1 + num_people_show2 + num_people_show3

weighted_sum = (num_people_show1 * avg_rating_show1 + 
                num_people_show2 * avg_rating_show2 + 
                num_people_show3 * avg_rating_show3)

overall_average_rating = weighted_sum / total_people

print(f"The overall average rating for the show is {overall_average_rating:.2f}")

# Add 1
N = int(input().strip())
denominations = [100, 50, 10, 5, 2, 1]
count_notes = 0

for denomination in denominations:
    count_notes += N // denomination
    N = N % denomination

print(count_notes)

# Add 2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
n = int(input("Enter the value of n for shift operations: "))

_and = a & b
_or = a | b
_not_a = ~a
_right_shift = a >> n
_left_shift = a << n
_xor = a ^ b

print(f"a AND b = {_and}")
print(f"a | b = {_or}")
print(f"~a = {_not_a}")
print(f"a Right Shift by n = {_right_shift}")
print(f"a Left Shift by n = {_left_shift}")
print(f"a ^ b = {_xor}")

# Add 3
n = int(input())
array = input().split()

for i in range(n):
    array[i] = int(array[i])

ones = 0
twos = 0

for num in array:
    twos |= ones & num
    
    ones ^= num
    
    threes = ones & twos
    
    ones &= ~threes
    twos &= ~threes

print(ones)
