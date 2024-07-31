import datetime
from os.path import exists

def main_menu():
    while True:
        print("\nBooking Management System")
        print("\n1. Booking")
        print("2. Report")
        print("3. Edit Booking")
        print("4. Delete Booking")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '1':
            AddBooking()
        elif choice == '2':
            report_menu()
        elif choice == '3':
            edit_booking()
        elif choice == '4':
            delete_booking()  
        elif choice == '5':    
            print("\nExiting the program\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def report_menu():
    while True:
        print("\nReport Menu")
        print("1. Today")
        print("2. This Week")
        print("3. This Month")
        print("4. Back to Main Menu")

        duration = input("\nSelect the duration of the report (1/2/3/4): ")


        if duration in ['1', '2', '3']:
            report_date = datetime.date.today()  # Set report_date to current date   <===================================

            if duration == '1':
                fetch_and_display_bookings('today', report_date)
            elif duration == '2':
                fetch_and_display_bookings('week', report_date)
            elif duration == '3':
                fetch_and_display_bookings('month', report_date)
        elif duration == '4':
            print()
            # main_menu()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def fetch_and_display_bookings(duration, report_date):
    print("\nFetching bookings...")

    try:
        with open('Capstone/Booking.txt', 'r') as file:
            next(file)  


            if duration == 'today':

                print("\n\t\t\t\tReport For Today")
                print("  Customer Name           | Start Date | End Date   | Driver              | Driver Phone Number | No. of Seats | Rental Fee (RM)")
                print("--------------------------------------------------------------------------------------------------------------------------------")

                for line in file:
                    fields = line.strip().split('|')
                    if len(fields) >= 8:
                        name = fields[0].strip()  
                        start_date = fields[8].strip()
                        end_date = fields[9].strip()
                        driver = fields[6].strip()
                        driver_phone = fields[7].strip()
                        seats = fields[4].strip()
                        fee = fields[10].strip()
                        
                        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()



                        if (report_date):
                            print(f"{name:<25} | {start_date} | {end_date} | {driver:<19} | {driver_phone:<19} | {seats:<12} | {fee}")       

                              

            elif duration == 'week':
                print("\n\t\t\t\tReport For This Week")
                print("  Customer Name           | Start Date | End Date   | Driver              | Driver Phone Number | No. of Seats | Rental Fee (RM)")
                print("--------------------------------------------------------------------------------------------------------------------------------")
                week_start = report_date - datetime.timedelta(days=6)  # Start of the current week
                for line in file:
                    fields = line.strip().split('|')
                    if len(fields) >= 8:
                        name = fields[0].strip()  
                        start_date = fields[8].strip()
                        end_date = fields[9].strip()
                        driver = fields[6].strip()
                        driver_phone = fields[7].strip()
                        seats = fields[4].strip()
                        fee = fields[10].strip()
                        
                        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()


                        #if week_start <= start_date <= report_date: # <===================

                        if (week_start <= start_date <= report_date):                             
                            print(f"{name:<25} | {start_date} | {end_date} | {driver:<19} | {driver_phone:<19} | {seats:<12} | {fee}")

                

            elif duration == 'month':
                print("\n\t\t\t\tReport For This Month")
                print("  Customer Name           | Start Date | End Date     | Driver              | Driver Phone Number | No. of Seats | Rental Fee (RM)")
                print("----------------------------------------------------------------------------------------------------------------------------------")
                month_start = report_date - datetime.timedelta(days=30)  # Start of the current month
                for line in file:
                    fields = line.strip().split('|')
                    if len(fields) >= 8:
                        name = fields[0].strip()  
                        start_date = fields[8].strip()
                        end_date = fields[9].strip()
                        driver = fields[6].strip()
                        driver_phone = fields[7].strip()
                        seats = fields[4].strip()
                        fee = fields[10].strip()
                        
                        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

                        

                        if (month_start <= start_date <= report_date):                            
                            print(f"{name:<25} | {start_date} | {end_date} | {driver:<19} | {driver_phone:<19} | {seats:<12} | {fee}")
                
                        
    except FileNotFoundError:
        print("Booking.txt not found. Please ensure the file exists.")

def append_booking(customer, seats, car, driver, start_date, end_date,  rental_fee):
    booking_details = f"{customer[1]:<20} | {customer[2]:^21} | {car[1]:<10} | {car[0]:<12} | {car[5]:^10} | {car[6]:<11} | {driver[2]:<19} | {driver[3]:^19} | {start_date} | {end_date:<10} | {rental_fee:^1}\n"

    try:
        file_exists = exists('Capstone/Booking.txt')
        with open('Capstone/Booking.txt', 'a') as file:
            if not file_exists:
                file.write(f"{'Customer':^20} | {'Customer Phone Number':^21} | {'Brand':^10} | {'Plate Number':^12} | {'Seats':^10} | {'Rental Rate':^11} | {'Driver':^19} | {'Driver Phone Number':^19} | {'Start Date'} | {'End Date':<10} | {'Rental Fee (RM)':^1}\n")
            file.write(booking_details)
        print("\nBooking has been successfully added.")


        Balik = input("\nDo you want to add more (Y/N)?")

        if (Balik.lower() == 'y'):
            AddBooking()

        elif(Balik.lower() == 'n'):
            print()
            # main_menu()
            return #False 


    except FileNotFoundError:
        print("Booking.txt not found. Please ensure the file exists.")

def edit_booking():
    try:
        with open('Capstone/Booking.txt', 'r') as file:
            lines = file.readlines()
            
        if len(lines) <= 1:
            print("No bookings available to edit.")
            return

        print()
        print("No. |  Start Date | End Date   | Customer Name         |  Driver              | Driver Phone Number | No. of Seats | Rental Fee (RM)")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        for idx, line in enumerate(lines[1:], start=1):  # start=1 to align with displayed numbers
            fields = line.strip().split('|')
            if len(fields) >= 10:
                name = fields[0].strip()
                start_date = fields[8].strip()
                end_date = fields[9].strip()
                driver = fields[6].strip()
                driver_phone = fields[7].strip()
                seats = fields[4].strip()
                fee = fields[10].strip()
                print(f"{idx - 1:<3} | {start_date:<11} | {end_date:<10} | {name:<21} | {driver:<20} | {driver_phone:<19} | {seats:<12} | {fee}")

        select = input("\nEnter the number of the booking you want to edit or 'b' to return to main menu: ")

        if select.lower() == 'b':
            print()
            # main_menu()
            return 

        selection = int(select) + 1

        # Adjust selection to account for header line
        if 1 <= selection < len(lines):
            selected_booking = lines[selection]
            print(f"\nSelected booking: \n")

            fields = selected_booking.strip().split('|')
            customer_name = fields[0].strip()
            start_date = fields[8].strip()
            end_date = fields[9].strip()
            driver = fields[6].strip()
            driver_phone = fields[7].strip()
            seats = fields[4].strip()
            fee = fields[10].strip()

            print(f"Customer     : {customer_name}")
            print(f"Booking Date : ({start_date}) - ({end_date})")
            print(f"Car          : {fields[2].strip()}")
            print(f"Driver       : {driver}")
            print(f"Rental Fee   : RM {fee}")
            
            print("\nEnter new dates for the booking (YYYY-MM-DD format):")

            while True:
                new_start_date = input(f"\nStart Date ({start_date}): ").strip() or start_date
                new_end_date = input(f"End Date ({end_date}): ").strip() or end_date

                try:
                    start_date_dt = datetime.datetime.strptime(new_start_date, '%Y-%m-%d')
                    end_date_dt = datetime.datetime.strptime(new_end_date, '%Y-%m-%d')

                    if start_date_dt >= end_date_dt:
                        print("End date must be after the start date. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid date format. Please enter the dates in YYYY-MM-DD format.")

            booking_duration = (end_date_dt - start_date_dt).days
            rental_rate = float(fields[5].strip())
            new_fee = booking_duration * rental_rate
            
            lines[selection] = f"{customer_name:<20} |{fields[1]:^21}|{fields[2]:^10}|{fields[3]:^12}| {seats:^10} |{fields[5]:^11}| {driver:<19} | {driver_phone:^19} | {new_start_date} | {new_end_date:<10} | {new_fee:^1}\n"

            # lines[selection] = f"{customer_name:<20} |{fields[1]}|{fields[2]}|{fields[3]}| {seats:^5} |{fields[5]:>5}| {driver} | {driver_phone} | {new_start_date} | {new_end_date} | {new_fee:}\n"

            with open('Capstone/Booking.txt', 'w') as file:
                file.writelines(lines)

            print("\n  Start Date | End Date   | Customer Name         |  Driver              | Driver Phone Number | No. of Seats | Rental Fee (RM)")
            print("--------------------------------------------------------------------------------------------------------------------------------------")
            print(f" {new_start_date:<11} | {new_end_date:<10} | {customer_name:<21} | {driver:<20} | {driver_phone:<19} | {seats:<12} | {new_fee}")

            print("\nBooking has been successfully updated.")
        else:
            print("Invalid selection. Please enter a valid number.")

    except FileNotFoundError:
        print("Booking.txt not found. Please ensure the file exists.")
def delete_booking():
    print("\n\t\t\t\tDelete Booking")
    try:
        with open('Capstone/Booking.txt', 'r') as file:
            lines = file.readlines()

        if len(lines) <= 1:
            print("No bookings available to delete.")
            return
        
        print()
        print("No. |  Start Date | End Date   | Customer Name         |  Driver              | Driver Phone Number | No. of Seats | Rental Fee (RM)")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        for idx, line in enumerate(lines[1:], start=1):
            fields = line.strip().split('|')
            if len(fields) >= 11:
                name = fields[0].strip()
                start_date = fields[8].strip()  
                end_date = fields[9].strip()    
                driver = fields[6].strip()      
                driver_phone = fields[7].strip() 
                seats = fields[4].strip()
                fee = fields[10].strip()         
                print(f"{idx - 1:<3} | {start_date:<11} | {end_date:<10} | {name:<21} | {driver:<20} | {driver_phone:<19} | {seats:<12} | {fee}")

        select = input("\nEnter the number of the booking you want to delete or 'b' to return to main menu: ")

        if (select.lower() == 'b'):
            return 
        
        selection = int(select) + 1

        if 1 <= selection <= len(lines):
            selected_booking = lines[selection]
            fields = selected_booking.strip().split('|')
            customer_name = fields[0].strip()
            start_date = fields[8].strip()  
            end_date = fields[9].strip()    

            print(f"\nCustomer     : {customer_name}")
            print(f"Booking Date : ({start_date}) - ({end_date})")

            areusure = input("\nAre you sure want to delete this booking (Y/N): ").strip().lower()

            if areusure == 'y':
                lines.pop(selection)
                
                with open('Capstone/Booking.txt', 'w') as file:
                    file.writelines(lines)
                
                print("\nBooking has been successfully deleted.")
            else:
                print("Booking deletion canceled.")
        else:
            print("Invalid selection. Please enter a valid number.")
    except FileNotFoundError:
        print("Booking.txt not found. Please ensure the file exists.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")        

def AddBooking():
    def select_customer():
        print("\n\t\t\t\tSelect a Customer by Number\n")
        print("  No. | Customer Name          | Phone Number  | Email                     | ID Number")
        print("---------------------------------------------------------------------------------------------")
        
        file_path = 'Capstone/Customers.txt'
        
        try:
            with open(file_path, 'r') as file:
                next(file)  # Skip header line
                customers = []
                for idx, line in enumerate(file, start=0):
                    fields = line.strip().split('|')
                    if len(fields) == 5:
                        customer_name = fields[1].strip()
                        phone_number = fields[2].strip()
                        email = fields[3].strip()
                        id_number = fields[4].strip()
                        customers.append((idx, customer_name, phone_number, email, id_number))
                        print(f" {idx:<4} | {customer_name:<22} | {phone_number:<13} | {email:<25} | {id_number}")
            
        except FileNotFoundError:
            print("Customer.txt not found. Please ensure the file exists.")
            return None

        while True: 
            select = input("\nSelect the number of customer or 'b' to return to the main menu: ")
            if (select.lower() == 'b'):
                print()
                # main_menu()
                break

            try:
                selection = int(select)
                if 1 <= selection <= len(customers):
                    selected_customer = customers[selection - 1]
                    print(f"\nCustomer Name  : {selected_customer[1]}")
                    print(f"Phone Number   : {selected_customer[2]}")
                    print(f"Email Addres   : {selected_customer[3]}")
                    print(f"ID Number      : {selected_customer[4]}")
                    return selected_customer
                # elif (selection == 'b'):
                #     main_menu()
                else:
                    print("Invalid selection. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_car(seats):
        print(" Plate   | Brand   | Model | Colour | Availability | No. of Seats   | Rental rate (RM/Day)")
        print("------------------------------------------------------------------------------------------")
        try:
            with open('Capstone/Cars.txt', 'r') as file:
                next(file)  # Skip header line
                available_cars = []
                for line in file:
                    fields = line.strip().split('|')
                    if len(fields) >= 7 and int(fields[5].strip()) == seats:
                        plate = fields[0].strip()
                        brand = fields[1].strip()
                        model = fields[2].strip()
                        colour = fields[3].strip()
                        available = fields[4].strip()
                        rental_rate = float(fields[6].strip())
                        available_cars.append((plate, brand, model, colour , available, seats, rental_rate))
                        print(f" {plate} | {brand:<7} | {model:<5} | {colour:<6} | {available:<12} | {seats:^13}  | {rental_rate:>10}")
            
        except FileNotFoundError:
            print("Cars.txt not found. Please ensure the file exists.")
            return None
        
        selected_model = input("\nEnter the brand of the car you want to select or 'b' to return to main menu: ").strip()

        if (selected_model.lower() == 'b'):
            print()
            # main_menu()
            return
        
        model_cars = [car for car in available_cars if car[1].lower() == selected_model.lower()]

        if not model_cars:
            print(f"No cars available for the brand: {selected_model} \n")
            return select_car(seats)

        print(f"\nAvailable cars for brand {selected_model}:")
        print(" Plate   | Brand   | Model | Colour | No. of Seats   | Rental rate (RM/Day) | Availability")
        print("------------------------------------------------------------------------------------------")
        for car in model_cars:
            print(f" {car[0]} | {car[1]:<7} | {car[2]:<5} | {car[5]:<6} | {car[5]:^13}  | {car[6]:^20} | {car[4]:>10}")

        while True:
            selected_plate = input("\nEnter the plate number of the car you want to select or 'b' to return to main menu: ").strip().upper()

            if (selected_plate.lower() == 'b'):
                print()
                # main_menu()
                break

            for car in model_cars:
                for car in available_cars:            
                    if car[0] == selected_plate:
                        if car[4].lower() == "available":
                            print(f"\nYou have selected Car: {car[1]} {car[2]}, Plate: {car[0]}")
                            return car
                        else:
                            print("The car is not available, please select again that available.\n")
                            return select_car(seats)
                             

            print("Invalid plate number. Please enter a valid plate number from the list.")

            # print("Invalid plate number. Please enter a valid plate number from the list.")
                            
    def select_driver():
        print("\n\t\t\t\tSelect a Driver by Number")
        print("  No. | Driver ID | Name                  | Phone Number | Email                     | Driving License")
        print("-------------------------------------------------------------------------------------------------------")
        try:
            with open('Capstone/Drivers.txt', 'r') as file:
                next(file)  # Skip header line
                drivers = []
                for idz, line in enumerate(file, start=0):
                    fields = line.strip().split('|')
                    if len(fields) >= 5:
                        driver_id = fields[0].strip()
                        name = fields[1].strip()
                        phone_number = fields[2].strip()
                        email = fields[3].strip()
                        driving_license = fields[4].strip()
                        drivers.append((idz, driver_id, name, phone_number, email, driving_license))
                        print(f" {idz:<4} | {driver_id:<9} | {name:<21} | {phone_number:<12} | {email:<25} | {driving_license}")
            
        except FileNotFoundError:
            print("Driver.txt not found. Please ensure the file exists.")
            return None
        
        while True:
            try:
                select = input("\nEnter the number of the driver you want to select or 'b' to return to main menu: ")

                if (select.lower() == 'b'):
                    print()
                    # main_menu()
                    break

                selection = int(select)

                if 1 <= selection <= len(drivers):
                    selected_driver = drivers[selection - 1]
                    print(f"\nYou have selected Driver: {selected_driver[2]}")
                    return selected_driver
                else:
                    print("Invalid selection. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
        selected_customer = select_customer()
        
        if not selected_customer:
            return
        
        start_date = input("\nEnter start date (YYYY-MM-DD) or 'b' to cancel: ") #"2024-09-09"

        if (start_date.lower() == 'b'):
            print()
            # main_menu()
            return

        end_date =  input("Enter end date (YYYY-MM-DD) or 'b' to cancel: ") #"2024-09-19"

        if (end_date.lower() == 'b'):
            print()
            # main_menu()
            return

        try:
            start_date_dt = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d')

            if start_date_dt >= end_date_dt:
                print("End date must be after the start date. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the dates in YYYY-MM-DD format.")
    
    if selected_customer:
        seater = input("\nEnter the number of seats of cars (4, 5, 7) or 'b' to return to main menu: ")

        if (seater.lower() == 'b'):
            print()
            # main_menu()
            return 

        seats = int(seater)
        if seats:
            selected_car = select_car(seats)
            if selected_car:
                selected_driver = select_driver()
                if selected_driver:
                    booking_duration = (end_date_dt - start_date_dt).days
                    rental_rate = selected_car[6]
                    rental_fee = booking_duration * rental_rate
                    print(f"Customer: {selected_customer[1]}")
                    print(f"Seats: {seats}")
                    print(f"Selected Car: {selected_car}")
                    print(f"Selected Driver: {selected_driver}")
                    print(f"Rental Fee: RM {rental_fee}")
                    append_booking(selected_customer, seats, selected_car, selected_driver, start_date, end_date, rental_fee)

main_menu()