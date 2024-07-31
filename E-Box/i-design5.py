# 1
def average_word_length(filename):
    with open(filename, 'r') as file:
        text = file.read()
        
    words = text.split()
    total_length = sum(len(word) for word in words)
    average_length = total_length // len(words)
    
    print(average_length)

average_word_length('averageLength.txt')

# 2
def sum_integers_in_file(filename):
    with open(filename, 'r') as file:
        numbers = file.readlines()
        
    total_sum = sum(int(number.strip()) for number in numbers)
    return total_sum

filename = 'sample.txt'
total_sum = sum_integers_in_file(filename)
print(f"The sum of the integers in the file {filename} is:{total_sum}")

# 3
def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = 'input.txt'
num_lines = count_lines_in_file(filename)
print(f'The file has {num_lines} lines')

# 4
def reverse_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        content = file.read()
    
    reversed_content = content[::-1]
    
    with open(output_filename, 'w') as file:
        file.write(reversed_content)

input_filename = 'input.txt'
output_filename = 'output.txt'
reverse_file(input_filename, output_filename)

# 5
def read_and_print_csv(input_filename):
    with open(input_filename, 'r') as file:
        content = file.readlines()
    
    for line in content:
        print(line.strip().replace(',', ';'))

input_filename = 'SalariesDataSet.csv'
read_and_print_csv(input_filename)

# I-asses 1
def count_letter_frequency(filename):
    frequency = {}
    
    with open(filename, 'r') as file:
        content = file.read().lower()  
    
    for char in content:
        if char.isalpha(): 
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    sorted_frequency = dict(sorted(frequency.items()))
    
    for letter, count in sorted_frequency.items():
        print(f'{letter}: {count}')

filename = 'frequencyFile.txt'
count_letter_frequency(filename)

# I-asses 2
def write_to_csv():
    import csv
    
    n = int(input("Enter the number of persons: "))
    
    data = []
    for _ in range(n):
        name = input("Enter the name: ")
        salary = input("Enter the salary: ")
        data.append([name, salary])
    
    filename = 'salaryData.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
    
    with open(filename, 'r') as csvfile:
        content = csvfile.read()
        print(content)

write_to_csv()


