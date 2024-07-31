# # 1
# from Person import Person

# def main():
#     print("Enter name")
#     name = input()
#     print("Enter age")
#     age = int(input())
    
#     person = Person(name, age)
    
#     print("Person Details")
#     print(person.name)
#     print(person.age)

# if __name__ == "__main__":
#     main()

# # 2
# from Person1 import Person

# print("Creating object using __init__ method")
# person_name = input("Enter name\n")
# person_age = input("Enter age\n")
# person1 = Person(person_name, person_age)
# print("Person Details")
# print(person1)
# print("\n")

# print("Creating object using class method")
# person_str = input("Enter name and age in comma separated format\n")
# person2 = Person.from_string(person_str)
# print("Person Details")
# print(person2)

# # 3
# from Person2 import Person
# from Address import Address

# print("Enter name")
# name = input()

# print("Enter age")
# age = input()

# print("Enter address")
# print("Enter street")
# street = input()

# print("Enter city")
# city = input()

# print("Enter state")
# state = input()

# address = Address(street, city, state)
# person = Person(name, age, address)

# print("Person Details")
# print(person)

# # 4
# from City import City
# from State import State

# state_list = [
#     State("Tamilnadu", []),
#     State("Andhra", []),
#     State("Karnataka", []),
#     State("Kerala", [])
# ]

# print("Enter City Details")
# city_created_list = []
# choice = "Yes"
# while choice.lower() == "yes":
#     city_name = input("Enter city name\n")
#     state_name = input("Enter state name\n")
#     state_found_flag = False
#     for state in state_list:
#         if state_name == state.name:
#             city = City(city_name, state)
#             state.city_list.append(city)
#             city_created_list.append(city)
#             state_found_flag = True
#             break
#     if not state_found_flag:
#         new_state = State(state_name, [])
#         state_list.append(new_state)
#         city = City(city_name, new_state)
#         city_created_list.append(city)
#         new_state.city_list.append(city)
#     choice = input("Do you want to add another city? Type Yes / No\n")

# print("\nCity Details\n")
# for city in city_created_list:
#     print(city)

# print("\nState Details\n")
# for state in state_list:
#     print(state)


# # 5
# from User import User

# print("Enter the details of User 1")
# name_1 = input("Name :\n")
# username_1 = input("Username :\n")
# pwd_1 = input("Password :\n")
# mobile_number_1 = input("Mobile Number :\n")

# print("Enter the details of User 2")
# name_2 = input("Name :\n")
# username_2 = input("Username :\n")
# pwd_2 = input("Password :\n")
# mobile_number_2 = input("Mobile Number :\n")

# # Create User objects
# user1 = User(name_1, username_1, pwd_1, mobile_number_1)
# user2 = User(name_2, username_2, pwd_2, mobile_number_2)

# # Compare the users based on mobile number
# if user1 == user2:
#     print("User 1 and User 2 are equal")
# else:
#     print("User 1 and User 2 are not equal")


# 6
# # 7
# from Student import Student

# u_id = int(input("Enter the student id\n"))
# username = input("Enter the student's username\n")
# password = input("Enter the password\n")
# name = input("Enter the name of the student\n")
# address = input("Enter the address\n")
# city = input("Enter the city\n")
# pincode = int(input("Enter the pincode\n"))
# contact_number = int(input("Enter the contact number\n"))
# email = input("Enter the email id\n")

# student = Student(u_id, username, password, name, address, city, pincode, contact_number, email)
# print(student)


# # 8
# from Employee import Employee
# from Developer import Developer
# from Manager import Manager
# from Utility import Utility

# manager_list = [
#     Manager("Arun", 80000),
#     Manager("Babu", 100000),
#     Manager("Chandru", 60000),
#     Manager("Deva", 60000)
# ]

# input_obj_list = []
# choice = "yes"
# while choice.lower() == "yes":
#     print("Menu\n1)Employee\n2)Developer")
#     choice1 = input("\nEnter choice\n")
#     if choice1 == "1":
#         input_str = input("Enter Employee details in comma separated format\n")
#         name, pay = input_str.split(",")
#         employee = Employee(name, int(pay))
#         input_obj_list.append(employee)
#         mgr_name = input("Enter manager name\n")
#         for manager in manager_list:
#             if manager.name == mgr_name:
#                 manager.add_employee(employee)
#     elif choice1 == "2":
#         input_str = input("Enter Developer details in comma separated format\n")
#         name, pay, prog_lang = input_str.split(",")
#         developer = Developer(name, int(pay), prog_lang)
#         input_obj_list.append(developer)
#         mgr_name = input("Enter manager name\n")
#         for manager in manager_list:
#             if manager.name == mgr_name:
#                 manager.add_employee(developer)
#     choice = input("Do you want to continue? Type yes/no\n")

# print("\nManager and Employee Allocation List")
# Utility.print_employees_under_each_manager(manager_list)


# 9
# class College:
#     def __str__(self, id=None, name=None, city=None, state=None, pincode=None,
#                 contact=None, email=None):
#         if id is not None and name is not None and city is not None and state is not None and pincode is not None:
#             return f"id : {id},Name : {name},City : {city},State : {state},Pincode : {pincode}"
#         elif name is not None and contact is not None and email is not None:
#             return f"Name : {name},Contact Number : {contact},Email : {email}"
#         else:
#             return "Invalid parameters"

# college = College()

# print("1. Enter College address and Display")
# print("2. Enter  the contact details and Display")
# print("3. exit")
# while True:
#     choice = input("\nEnter your choice\n")
    
#     if choice == "1":
#         id = input("Enter the College id\n")
#         name = input("Enter the College name\n")
#         city = input("Enter the City\n")
#         state = input("Enter the State\n")
#         pincode = input("Enter the Pincode\n")
#         # print(college.__str__(id=id, name=name, city=city, state=state, pincode=pincode))
#         print(f"id : {id}")
#         print(f"Name : {name}")
#         print(f"City : {city}")
#         print(f"State : {state}")
#         print(f"Pincode : {pincode}")

#     elif choice == "2":
#         name = input("Enter the name of the College\n")
#         contact = input("Enter the contact number\n")
#         email = input("Enter the email id\n")
#         # print(college.__str__(name=name, contact=contact, email=email))
#         print(f"Name : {name}")
#         print(f"Contact Number : {contact}")
#         print(f"Email : {email}")

#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")


# 10
from Person3 import Person

person_first_name = input("Enter first name\n")
person_last_name = input("Enter last name\n")
person_age = input("Enter age\n")
person = Person(person_first_name, person_last_name, person_age)
print("Full name of the person is ",person.fullname())
print("Person Details")
print(person)
	
