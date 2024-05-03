class Person:
    """ A class that represent any person"""

    # Constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # A function that prints the first and last name
    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}"


class Employee(Person):
    """A class that represents an employee"""
    employee_count = 0

    # Constructor
    def __init__(self, first_name, last_name, employee_type, department, job_title, basic_salary, manager_id, age,
                 date_of_birth, passport_details):
        super().__init__(first_name, last_name)
        Employee.employee_count += 1
        self.employee_id = f"E{Employee.employee_count}"  # Generate employee ID automatically
        self.employee_type = employee_type
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.manager_id = manager_id
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    def set_employee_id(self, id):
        self.employee_id = id

    # A function that prints the details of an employee
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, ID: {self.employee_id}, Type: {self.employee_type.value}, Department: {self.department}, Job Title: {self.job_title}, Basic Salary: {self.basic_salary}, Manager ID: {self.manager_id}, Age: {self.age}, Date of Birth: {self.date_of_birth}, Passport Details: {self.passport_details}"


class Client(Person):
    """A class that represents a client"""
    client_count = 0

    def __init__(self, first_name, last_name, address, contact_details, budget):
        super().__init__(first_name, last_name)
        Client.client_count += 1
        self.client_id = f"C{Client.client_count}"  # Generate client ID automatically
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def set_client_id(self, id):
        self.client_id = id

    def __str__(self):
        return f"Client: {self.first_name} {self.last_name}, ID: {self.client_id}, Address: {self.address}, Contact Details: {self.contact_details}, Budget: {self.budget}"


class Guest(Person):
    """A class that represents a guest"""
    guest_count = 0

    def __init__(self, first_name, last_name, address, contact_details):
        super().__init__(first_name, last_name)
        Guest.guest_count += 1
        self.guest_id = f"G{Guest.guest_count}"  # Generate guest ID automatically
        self.address = address
        self.contact_details = contact_details

    def set_guest_id(self, id):
        self.guest_id = id

    def __str__(self):
        return f"Guest: {self.first_name} {self.last_name}, ID: {self.guest_id}, Address: {self.address}, Contact Details: {self.contact_details}"