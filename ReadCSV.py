import csv
from Package import Package
# Seperate file to read the CSV data

# Reads the CSV file containing distance information
with open("CSV/DISTANCE.csv") as distance_csv:
    Distance = csv.reader(distance_csv)
    Distance = list(Distance)

    # Reads the CSV file containing address information
with open("CSV/ADDRESS.csv") as address_csv:
    Address = csv.reader(address_csv)
    Address = list(Address)

    # Reads the CSV file containing package information
with open("CSV/PACKAGE.csv") as package_csv:
    PackageCSV = csv.reader(package_csv)
    PackageCSV = list(PackageCSV)

# the total time complexity of the provided code is O(n),
# where n is the number of rows in the largest CSV file among DISTANCE.csv, ADDRESS.csv, and PACKAGE.csv.
