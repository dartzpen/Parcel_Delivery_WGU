
from HashMap import ChainingHash
import csv
# Define the Package class to represent package information
# Time Complexity: O(1)


class Package:
    def __init__(self, package_id, delivery_address, city, state, zipcode, deadline, weight, delivery_status):
        # Initialize package attributes
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline
        self.weight = weight
        self.delivery_status = delivery_status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        # Return a string representation of the package
        return "Package ID: %s | Address: %s | City: %s | State: %s | Zipcode: %s | Deadline: %s | Weight: %s | " \
               "Estimated Delivery Time: %s | Status: %s |" % (self.package_id, self.delivery_address, self.city, self.state,
                                                     self.zipcode, self.deadline_time, self.weight,
                                                     self.delivery_time, self.delivery_status)

    def update_delivery_status(self, current_time):
        # Update the delivery status based on the current time
        if self.delivery_time < current_time:
            self.delivery_status = "Delivered at " + str(self.delivery_time)
        elif self.departure_time > current_time:
            self.delivery_status = "En route"
        else:
            self.delivery_status = "At Hub"

# Loading package data into a hash table:
# Time Complexity: O(n). (Since there are n rows in the CSV file, the time complexity is linear with respect to the number of rows.)


def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline_time = package[5]
            package_weight = package[6]
            package_status = "At Hub"

            # Create a Package object with the extracted data
            p = Package(package_id, package_address, package_city, package_state, package_zipcode,
                        package_deadline_time, package_weight, package_status)

            # Insert the Package object into the hash table using the package_id as the key
            package_hash_table.insert(package_id, p)


# Create an instance of the ChainingHash class
packagehash = ChainingHash()


# Load packages into the hash table from the "PACKAGE.csv" file
load_package_data("CSV/PACKAGE.csv", packagehash)
