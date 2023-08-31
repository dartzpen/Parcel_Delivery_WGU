import datetime
from ReadCSV import Address
from ReadCSV import Distance
from Package import packagehash

# Extract the address number from the address string

# Time Complexity: O(n)


def get_address_number(address):
    for row in Address:
        if address in row[2]:
            return int(row[0])

# Calculate the distance between two addresses

# Time Complexity: O(1)


def calculate_distance(source_address, destination_address):
    distancebetween = Distance[source_address][destination_address]
    if distancebetween == '':
        distancebetween = Distance[destination_address][source_address]

    return float(distancebetween)

# Class for trucks

# Time Complexity: O(1)
# The constructor initializes attributes directly. Assigning values to attributes takes constant time.


class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                               self.address, self.depart_time)

# Optimize the delivery route for a given truck using the Nearest Neighboor Algorithm
# Time Complexity: O(n^2)
# The function iterates through undelivered packages to find the nearest package for each package.
# For each undelivered package, it calculates the distance to all other undelivered packages.
# This results in a nested loop structure, leading to a time complexity of O(n^2), where n is the number of undelivered packages.


def NearestNeighborRoute(truck):
    # Initialize an array to store undelivered packages
    undelivered = []

    # Populate the array with packages to be delivered
    for package_ID in truck.packages:
        # Search for package details using the package ID
        package = packagehash.search(package_ID)
        # Add the package to the list of undelivered packages
        undelivered.append(package)

    # Clear the list of packages that were initially assigned to the truck
    truck.packages.clear()

    # Begin the process of delivering packages using the Nearest Neighbor Algorithm
    while len(undelivered) > 0:
        # Initialize variables to track the nearest package and its distance
        nearest_distance = 2000
        nearest_package = None

        # Iterate through the undelivered packages to find the nearest one
        for package in undelivered:
            # Calculate the distance between the truck's current location and the package's address
            distance_to_package = calculate_distance(get_address_number(truck.address),
                                                     get_address_number(package.delivery_address))

            # Check if the current package is closer than the previously found nearest package
            if distance_to_package <= nearest_distance:
                # Update the nearest package and its distance
                nearest_distance = distance_to_package
                nearest_package = package

        # Assign the nearest package to the truck's list of packages for delivery
        truck.packages.append(nearest_package.package_id)

        # Remove the assigned package from the list of undelivered packages
        undelivered.remove(nearest_package)

        # Update the truck's mileage based on the distance driven to deliver the package
        truck.mileage += nearest_distance

        # Update the truck's current location to the address of the delivered package
        truck.address = nearest_package.delivery_address

        # Calculate the time it took for the truck to drive to the delivered package
        time_to_deliver = datetime.timedelta(hours=nearest_distance / 18)
        # Update the truck's time and record the package's delivery and departure times
        truck.time += time_to_deliver
        nearest_package.delivery_time = truck.time
        nearest_package.departure_time = truck.depart_time


# Create truck instances
# Time Complexity: O(1)
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
               datetime.timedelta(hours=8))

truck2 = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
               datetime.timedelta(hours=9, minutes=5))

# Overall, the dominant time complexity is associated with the NearestNeighborRoute function due to its nested loop structure, resulting in O(n^2) complexity.
# The rest of the operations involve constant time complexity or linear time complexity depending on the size of the data they are working with.

# Loading the trucks
NearestNeighborRoute(truck1)
NearestNeighborRoute(truck2)

# Ensure truck 3 departs only after the first two trucks have finished delivering
truck3.departure = min(truck1.time, truck2.time)
NearestNeighborRoute(truck3)
