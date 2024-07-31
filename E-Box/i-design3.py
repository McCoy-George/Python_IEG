# 1
N = int(input().strip())

even_count = 0
odd_count = 0

for i in range(N):
    code = int(input().strip())
    if code % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, odd_count)


# 2
N = int(input().strip())
primes = []
num = 2

while len(primes) < N:
    is_prime = True
    
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    num += 1

for i in range(len(primes)):
    if i == len(primes) - 1:
        print(primes[i])
    else:
        print(primes[i], end=' ')


# 3
count = int(input())

series = [30, 35]

first_difference = 5
second_difference = 3

first_decrementer = -2 
second_incrementer = 10


while len(series) < count:    
    next_number = series[len(series) - 1] + second_difference
    
    series.append(next_number)
    
    first_difference = first_difference + first_decrementer
    first_decrementer = first_decrementer - 2
    
    if (len(series) < count):
        
        then_next_number = series[len(series) - 1] + first_difference
        series.append(then_next_number)
        
    second_difference = second_difference + second_incrementer
    second_incrementer = second_incrementer + 2

for i in range(count):
    print(series[i], end=" ")


# 4
input_string = input().strip().split()
A = int(input_string[0])
B = int(input_string[1])
N = int(input_string[2])

richie_score = A
riya_score = B

for turn in range(1, N + 1):
    if turn % 2 == 1:
        richie_score *= 2
    else:
        riya_score *= 2

final_score = richie_score + riya_score

print(final_score)


# 5
N = int(input().strip())

if N < 10:
    print("Invalid Input")
else:
    str_N = str(N)
    
    first_digit = int(str_N[0])
    last_digit = int(str_N[-1])
    
    abs_difference = first_digit - last_digit
    
    if (abs_difference < 0):
        abs_difference = abs_difference * -1
        print(abs_difference)
    else:
        print(abs_difference)

# I-asses
a = int(input())
b = int(input())

primes = []

for num in range(a, b + 1):
    if num > 1:  
        is_prime = True
        if num == 2:  
            primes.append(num)
            continue
        if num % 2 == 0:  
            continue
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

for prime in primes:
    print(prime, end=" ")
