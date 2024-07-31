# 1 
def delete(name, n):
    index_to_delete = n - 1
    
    if 0 <= index_to_delete < len(name):
        modified_name = name[:index_to_delete] + name[index_to_delete + 1:]
        return modified_name
    else:
        return "Invalid index provided."

name = input()
n = int(input())

modified_name = delete(name, n)
print(modified_name)


# 2
def is_palindrome(input_string):
    return input_string == input_string[::-1]

def reverse_string(input_string):
    return input_string[::-1][3:]

def make_palindrome(input_string):
    if is_palindrome(input_string):
        return input_string
    
    reversed_string = reverse_string(input_string)
    
    palindrome = input_string[:3] + reversed_string
    
    return palindrome

input_string = input()

palindrome = make_palindrome(input_string)
print(palindrome)


# 3
def print_slash_pattern(n):
    pattern = '/' * n + '\\' * n + '/' * n + '\\' * n
    
    for _ in range(4):  
        print(pattern)

n = int(input())

print_slash_pattern(n)


# 4
def concatenate_strings(a,b):
    
    if a and b and a[0].lower() == b[0].lower():
        concatenated_string = a +  b
        return concatenated_string
    else:
        return "Invalid Input"
        
print("Enter the first string:")
str1 = input()
    
print("Enter the second string:")
str2 = input()

result = concatenate_strings(str1, str2)
print(result)


# 5
def birthday_gift():
    n = int(input().strip())
    
    total_students = 0
    for _ in range(n):
        total_students += int(input().strip())
    
    price = int(input().strip())
    
    total_books = total_students
    
    total_cost = total_books * price
    
    print(f"Total number of books required : {total_books}")
    print(f"Total cost: {total_cost}")

birthday_gift()


# 6
def symmetric_difference(set1, set2):
    set1 = set(map(int, set1.split(',')))
    set2 = set(map(int, set2.split(',')))

    if set1 == set2:
        return 'invalid set'
    else:
        return set(sorted(list(set1.symmetric_difference(set2))))

set1 = input()
set2 = input()

result = symmetric_difference(set1, set2)
print(result)


# 7
from datetime import datetime

def calculate_date_difference():
    date_format = "%b %d %Y %I:%M%p"
    first_date = input().strip()
    second_date = input().strip()
    
    first_date_parsed = datetime.strptime(first_date, date_format)
    second_date_parsed = datetime.strptime(second_date, date_format)
    
    difference = second_date_parsed - first_date_parsed
    
    days = difference.days
    total_seconds = difference.seconds
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"{days} days, {hours}:{minutes:02}:{seconds:02}")

calculate_date_difference()


# 8
def remove_duplicate():
    n = int(input("Enter total Number of sheets: "))
    
    attendance_sheets = []

    for i in range(n):
        sheet = tuple(map(int, input().split()))
        attendance_sheets.append(sheet)
    
    print("Attendance Sheets with Register Number:", tuple(attendance_sheets))
    
    unique_numbers = set()
    for sheet in attendance_sheets:
        unique_numbers.update(sheet)
    
    print("Final sheet:", tuple(sorted(unique_numbers)))

remove_duplicate()


# 9
def find_second_highest_mark():
    n = int(input())

    student_records = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_records[name] = marks

    student_name = input()

    if student_name in student_records:
        marks = student_records[student_name]

        if len(set(marks)) == 1:
            print(f"{student_name} scored same marks in all subjects: {int(marks[0])}")
        else:
            unique_marks = list(set(marks))
            unique_marks.sort(reverse=True)
            second_highest_mark = unique_marks[1]
            print(f"Second Highest mark of {student_name}: {int(second_highest_mark)}")
    else:
        print("Student doesn't exist")

find_second_highest_mark()


# 10
def word_count(sentence):
    words = sentence.split()
    word_dict = {}
    
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

sentence = input("Enter a sentence: ")

word_counts = word_count(sentence)

print(word_counts)


# I-Asses 1
def subset_and_superset(set1, set2):
    set1 = set(map(int, set1.split(',')))
    set2 = set(map(int, set2.split(',')))
    
    subset_1_to_2 = set1 <= set2
    subset_2_to_1 = set2 <= set1
    
    superset_1_to_2 = set1 >= set2
    superset_2_to_1 = set2 >= set1
    
    print("True" if subset_1_to_2 else "False")
    print("True" if subset_2_to_1 else "False")
    print("True" if superset_1_to_2 else "False")
    print("True" if superset_2_to_1 else "False")

input1 = input().strip()
input2 = input().strip()

subset_and_superset(input1, input2)


# I-Asses 2
def retrieve_client_details():
    print("Enter the number of clients")
    num_clients = int(input().strip())
    
    client_details = {}
    
    for i in range(1, num_clients + 1):
        print(f"Enter the details of the client {i}")
        name = input().strip()
        email = input().strip()
        passport_number = input().strip()
        client_details[passport_number] = (name, email, passport_number)
    
    print("Enter the passport number of the client to be searched")
    search_passport_number = input().strip()
    
    if search_passport_number in client_details:
        print("Client Details")
        details = client_details[search_passport_number]
        print(f"{details[0]}--{details[1]}--{details[2]}")
    else:
        print("Client not found")

retrieve_client_details()

