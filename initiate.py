from persistence import *
from persistence import repo, Branche, Supplier, Product, Employee
import sys
import os

def add_branche(splittedline: list):
    id = int(splittedline[0])
    location = splittedline[1]
    number_of_employees = int(splittedline[2])
    branche = Branche(id, location, number_of_employees)
    repo.branches.insert(branche)

def add_supplier(splittedline: list):
    id = int(splittedline[0])
    name = splittedline[1]
    contact_information = splittedline[2]
    supplier = Supplier(id, name, contact_information)
    repo.suppliers.insert(supplier)

def add_product(splittedline: list):
    id = int(splittedline[0])
    description = splittedline[1]
    price = float(splittedline[2])
    quantity = int(splittedline[3])
    product = Product(id, description, price, quantity)
    repo.products.insert(product)

def add_employee(splittedline: list):
    id = int(splittedline[0])
    name = splittedline[1]
    salary = float(splittedline[2])
    branche = int(splittedline[3])
    employee = Employee(id, name, salary, branche)
    repo.employees.insert(employee)

# Dictionary to map config file records to functions
adders = {
    "B": add_branche,
    "S": add_supplier,
    "P": add_product,
    "E": add_employee
}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)