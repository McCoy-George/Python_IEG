# Problem 1
total_volume = float(input("\nEnter the total volume of solution needed (liters): "))
desired_concentration = float(input("Enter the desired concentration (%): "))
concentration_a = float(input("Enter the concentration of Solution A (%): "))
concentration_b = float(input("Enter the concentration of Solution B (%): "))

a = concentration_a / 100
b = concentration_b / 100
c = desired_concentration * total_volume / 100

y = (c - a * total_volume) / (b - a)
x = total_volume - y

print(f"\nRequired liters of Solution A: {x:.2f}")
print(f"Required liters of Solution B: {y:.2f}")


stock_limit = 3  

if x <= stock_limit:
    print("\nSolution (A) is available, can proceed")
else:
    print(f"Solution (A) is not available, please order {x - stock_limit:.2f} liter now")

if y <= stock_limit:
    print("Solution (B) is available, can proceed")
else:
    print(f"Solution (B) is not available, please order {y - stock_limit:.2f} liter now\n")



# Problem 2
x = 0b10101100
y = 0b11011001

lower_4_bits_x = x & 0b1111
print("\nLower 4 bits of x:", bin(lower_4_bits_x))

y_is_even = (y & 1) == 0
print(f"\ny is {'even' if y_is_even else 'odd'}")

x &= 0b1111
print("\nx with upper 4 bits cleared:", bin(x))

if (y & 0b10000):
    print("\n5th bit of y is set.")
else:
    print("5th bit of y is not set.")


# Problem 3
worker1_time = float(input("Enter the time Worker A takes to complete the project (in hours): "))

worker2_time = float(input("Enter the time Worker B takes to complete the project (in hours): "))

combined_rate = 1 / worker1_time + 1 / worker2_time
    
time_to_complete = 1 / combined_rate

days = int(time_to_complete // 24)
hours = int(time_to_complete % 24)
minutes = int((time_to_complete - days * 24 - hours) * 60)

print("Time required for both workers to complete the project together:", days, "days,", hours, "hours,", minutes, "minutes")



# Problem 4
a = 0b10101000
b = 0b01010100

a_with_lower_bits_set = a | 0b00001111
print(f"\na with lower 4 bits set: {bin(a_with_lower_bits_set)}")

combined = a | b
print(f"\nCombined a and b using OR: {bin(combined)}")

mask = 0b00100010  
a_with_mask = a | mask
print(f"\na with 2nd and 6th bits set: {bin(a_with_mask)}")



# Problem 5
investment = float(input("Enter the total investment: "))
rate1 = float(input("Enter the interest rate for the first account (in %): "))
rate2 = float(input("Enter the interest rate for the second account (in %): "))
interest = float(input("Enter the total annual interest: "))

rate1 /= 100
rate2 /= 100

x = (interest - rate2 * investment) / (rate1 - rate2)
y = investment - x

print(f"Amount invested in the first account: RM{x:.2f}")
print(f"Amount invested in the second account: RM{y:.2f}")



# Problem 6:
x = 0b10101100
y = 0b11010010

x = x ^ y
y = x ^ y
x = x ^ y

print("After swapping, x =", bin(x))
print("After swapping, y =", bin(y))

x = x ^ (0b1 << 2) 
x = x ^ (0b1 << 4)  

print("After toggling, x =", bin(x))

a = 29
b = 15

if a != b:
    print("a and b are different.")
else:
    print("a and b are the same.")
