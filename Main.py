# C950 DATA STRUCTURES AND ALGORITHMS II
# Daisy Pennartz | Student ID: 011104619
import datetime
from DeliveryRoute import truck1
from DeliveryRoute import truck2
from DeliveryRoute import truck3
from Package import packagehash

# Main class that provides the user-interface

# most of the operations in the code involve O(1) time complexity,
# except for iterating through all package IDs (which is a constant number of iterations)


class Main:

    # Method that displays a border for readability
    @staticmethod
    def display_border():
        print('-' * 70)

    # Method in which the total mileage of the route is calculated
    @staticmethod
    def display_total_mileage():
        sum_mileage = truck1.mileage + truck2.mileage + truck3.mileage
        print(f"The total mileage for the current route is: {sum_mileage}")
    
    @staticmethod
    def display_truck_mileage(truck1, truck2, truck3):
        total_mileage_truck1 = truck1.mileage
        total_mileage_truck2 = truck2.mileage
        total_mileage_truck3 = truck3.mileage

        print(f"Total mileage for Truck 1: {round(total_mileage_truck1)}")
        print(f"Total mileage for Truck 2: {total_mileage_truck2}")
        print(f"Total mileage for Truck 3: {total_mileage_truck3}")

    # Method used to retrieve the desired timestamp from the user
    @staticmethod
    def get_user_time_input():
        user_time_input = input("Please enter a time in HH:MM format: ")
        try:
            hours, minutes = map(int, user_time_input.split(":"))
            user_timedelta = datetime.timedelta(hours=hours, minutes=minutes)
            return user_timedelta
        except ValueError:
            print("Invalid time format. Please re-run the program.")
            exit()

    # Method used to retrieve the desired Package ID from the user
    @staticmethod
    def get_package_id_input():
        try:
            package_id = int(input("Enter the numeric package ID: "))
            return package_id
        except ValueError:
            print("Invalid entry. Please re-run the program.")
            exit()
# ---------------------------- START OF USER INTERFACE ---------------------------------
    # Welcome message
    display_border()
    print("Welcome to WGUPS! (Western Governors University Parcel Service)")
    print("This program designs an efficient route for packages and allows for an easy package-tracking system.")
    display_border()

    # Displays the total route mileage upon starting the program
    display_total_mileage()
    display_border()

    # Display total mileage for individual trucks
    display_truck_mileage(truck1, truck2, truck3)
    display_border()

    # Prompts the user to choose an option to find the status of delivery
    text = input("Please type 'all' to check all packages delivery status, "
                 "or 'lookup' to look up an the status of the individual package:\n")
    display_border()

    # If user enters 'time':
    if text.lower() == "all":
        user_timedelta = get_user_time_input()
        try:
            for packageID in range(1, 41):
                package = packagehash.search(packageID)
                package.update_delivery_status(user_timedelta)
                print(str(package))
        except ValueError:
            print("Invalid entry. Please re-run the program.")
            exit()

    # If user Enters 'lookup':
    elif text.lower() == "lookup":
        try:
            package_id = get_package_id_input()
            package = packagehash.search(package_id)
            user_timedelta = get_user_time_input()
            package.update_delivery_status(user_timedelta)
            print(str(package))
            display_border()
        except ValueError:
            print("Invalid entry. Please re-run the program.")
            exit()
    else:
        print("Invalid entry. Please re-run the program.")
        exit()


# instance of main
main_instance = Main()
