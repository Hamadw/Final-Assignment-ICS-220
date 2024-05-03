from PersonClass import *
from EventClass import *
from SupplierClass import *
from VenueClass import *
import tkinter as tk
from tkinter import messagebox
import pickle

class CompanyManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Best Company Management System")
        self.create_widgets()

    def create_widgets(self):
        # Buttons to open different management windows
        tk.Button(self.root, text="Manage Employees", command=self.open_employee_management_window).pack(pady=10)
        tk.Button(self.root, text="Manage Events", command=self.open_event_management_window).pack(pady=10)
        tk.Button(self.root, text="Manage Clients", command=self.open_client_management_window).pack(pady=10)
        tk.Button(self.root, text="Manage Guests", command=self.open_guest_management_window).pack(pady=10)
        tk.Button(self.root, text="Manage Suppliers", command=self.open_supplier_management_window).pack(pady=10)

    def open_employee_management_window(self):
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Employee Management")

        # Add buttons
        tk.Button(employee_window, text="Create Employee", command=self.add_employee).grid(row=2, column=0, pady=10)
        tk.Button(employee_window, text="Delete Employee", command=self.delete_employee).grid(row=2, column=1, pady=10)
        tk.Button(employee_window, text="Modify Employee", command=self.modify_employee).grid(row=2, column=2, pady=10)
        tk.Button(employee_window, text="Display Employees", command=self.display_employees).grid(row=2, column=3,
                                                                                                  pady=10)

    def add_employee(self):
        # Create a new Toplevel window for adding employee details
        add_employee_window = tk.Toplevel(self.root)
        add_employee_window.title("Add Employee")

        # Add labels and entry fields for each attribute of the employee
        tk.Label(add_employee_window, text="First name:").grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(add_employee_window)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Last name:").grid(row=1, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(add_employee_window)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Employee Type:").grid(row=2, column=0, padx=5, pady=5)
        self.employee_type_entry = tk.Entry(add_employee_window)
        self.employee_type_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Department:").grid(row=3, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(add_employee_window)
        self.department_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Job Title:").grid(row=4, column=0, padx=5, pady=5)
        self.job_title_entry = tk.Entry(add_employee_window)
        self.job_title_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Basic Salary:").grid(row=5, column=0, padx=5, pady=5)
        self.basic_salary_entry = tk.Entry(add_employee_window)
        self.basic_salary_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Manager ID:").grid(row=6, column=0, padx=5, pady=5)
        self.manager_id_entry = tk.Entry(add_employee_window)
        self.manager_id_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Age:").grid(row=7, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(add_employee_window)
        self.age_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Date of Birth:").grid(row=8, column=0, padx=5, pady=5)
        self.date_of_birth_entry = tk.Entry(add_employee_window)
        self.date_of_birth_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(add_employee_window, text="Passport Details:").grid(row=9, column=0, padx=5, pady=5)
        self.passport_details_entry = tk.Entry(add_employee_window)
        self.passport_details_entry.grid(row=9, column=1, padx=5, pady=5)

        # Create a button to submit the employee details
        submit_button = tk.Button(add_employee_window, text="Submit", command=self.submit_employee)
        submit_button.grid(row=10, column=0, columnspan=2, padx=5, pady=10)

    def submit_employee(self):
        # Retrieve the entered values from the entry fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        employee_type = self.employee_type_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = float(self.basic_salary_entry.get())  # Assuming salary is entered as a float
        manager_id = self.manager_id_entry.get()
        age = int(self.age_entry.get())  # Assuming age is entered as an integer
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        # Create an Employee object
        employee = Employee(first_name, last_name, employee_type, department, job_title, basic_salary, manager_id, age,
                            date_of_birth, passport_details)

        # Save Employee object using Pickle
        with open("employees.pickle", "ab") as file:
            pickle.dump(employee, file)

        messagebox.showinfo("Success", "Employee added successfully")

    def delete_employee(self):
        # Create a new Toplevel window for deleting an employee
        delete_employee_window = tk.Toplevel(self.root)
        delete_employee_window.title("Delete Employee")

        # Add a label and entry field for entering the employee ID
        tk.Label(delete_employee_window, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5)
        self.employee_id_entry = tk.Entry(delete_employee_window)
        self.employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to delete the employee
        delete_button = tk.Button(delete_employee_window, text="Delete", command=self.confirm_delete_employee)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def confirm_delete_employee(self):
        # Retrieve the entered employee ID
        employee_id = self.employee_id_entry.get()

        # Confirm with the user before deletion
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete employee with ID {employee_id}?")

        if confirm:
            # Delete the employee with the specified ID
            try:
                with open("employees.pickle", "rb") as file:
                    employees = []
                    while True:
                        try:
                            employee = pickle.load(file)
                            if employee.employee_id != employee_id:
                                employees.append(employee)
                        except EOFError:
                            break
                with open("employees.pickle", "wb") as file:
                    for emp in employees:
                        pickle.dump(emp, file)
                messagebox.showinfo("Success", "Employee deleted successfully")
            except FileNotFoundError:
                messagebox.showwarning("Warning", "No employees found")

    def modify_employee(self):
        # Create a new Toplevel window for modifying an employee
        modify_employee_window = tk.Toplevel(self.root)
        modify_employee_window.title("Modify Employee")

        # Add labels and entry fields for the employee ID and new details
        tk.Label(modify_employee_window, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_employee_id_entry = tk.Entry(modify_employee_window)
        self.modify_employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add labels and entry fields for new employee details
        tk.Label(modify_employee_window, text="New First name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_first_name_entry = tk.Entry(modify_employee_window)
        self.new_first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Last name:").grid(row=2, column=0, padx=5, pady=5)
        self.new_last_name_entry = tk.Entry(modify_employee_window)
        self.new_last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Employee Type:").grid(row=3, column=0, padx=5, pady=5)
        self.new_employee_type_entry = tk.Entry(modify_employee_window)
        self.new_employee_type_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Department:").grid(row=4, column=0, padx=5, pady=5)
        self.new_department_entry = tk.Entry(modify_employee_window)
        self.new_department_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Job Title:").grid(row=5, column=0, padx=5, pady=5)
        self.new_job_title_entry = tk.Entry(modify_employee_window)
        self.new_job_title_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Basic Salary:").grid(row=6, column=0, padx=5, pady=5)
        self.new_basic_salary_entry = tk.Entry(modify_employee_window)
        self.new_basic_salary_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Manager ID:").grid(row=7, column=0, padx=5, pady=5)
        self.new_manager_id_entry = tk.Entry(modify_employee_window)
        self.new_manager_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Age:").grid(row=8, column=0, padx=5, pady=5)
        self.new_age_entry = tk.Entry(modify_employee_window)
        self.new_age_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Date of Birth:").grid(row=9, column=0, padx=5, pady=5)
        self.new_date_of_birth_entry = tk.Entry(modify_employee_window)
        self.new_date_of_birth_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(modify_employee_window, text="New Passport Details:").grid(row=10, column=0, padx=5, pady=5)
        self.new_passport_details_entry = tk.Entry(modify_employee_window)
        self.new_passport_details_entry.grid(row=10, column=1, padx=5, pady=5)

        # Create a button to modify the employee details
        modify_button = tk.Button(modify_employee_window, text="Modify", command=self.confirm_modify_employee)
        modify_button.grid(row=11, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_employee(self):
        # Retrieve the entered employee ID and new details
        employee_id = self.modify_employee_id_entry.get()
        new_first_name = self.new_first_name_entry.get()
        new_last_name = self.new_last_name_entry.get()
        new_employee_type = self.new_employee_type_entry.get()
        new_department = self.new_department_entry.get()
        new_job_title = self.new_job_title_entry.get()
        new_basic_salary = float(
            self.new_basic_salary_entry.get()) if self.new_basic_salary_entry.get() else None  # Check if value is provided
        new_manager_id = self.new_manager_id_entry.get()
        new_age = int(self.new_age_entry.get()) if self.new_age_entry.get() else None  # Check if value is provided
        new_date_of_birth = self.new_date_of_birth_entry.get()
        new_passport_details = self.new_passport_details_entry.get()

        # Modify the employee with the specified ID
        try:
            with open("employees.pickle", "rb") as file:
                employees = []
                employee_found = False  # Flag to check if employee with the specified ID is found
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee.employee_id == employee_id:
                            employee_found = True
                            # Update the employee details
                            if new_first_name:
                                employee.first_name = new_first_name
                            if new_last_name:
                                employee.last_name = new_last_name
                            if new_employee_type:
                                employee.employee_type = new_employee_type
                            if new_department:
                                employee.department = new_department
                            if new_job_title:
                                employee.job_title = new_job_title
                            if new_basic_salary is not None:
                                employee.basic_salary = new_basic_salary
                            if new_manager_id:
                                employee.manager_id = new_manager_id
                            if new_age is not None:
                                employee.age = new_age
                            if new_date_of_birth:
                                employee.date_of_birth = new_date_of_birth
                            if new_passport_details:
                                employee.passport_details = new_passport_details
                        employees.append(employee)
                    except EOFError:
                        break
            # Rewrite the pickle file with the modified employee details
            with open("employees.pickle", "wb") as file:
                for emp in employees:
                    pickle.dump(emp, file)
            if employee_found:
                messagebox.showinfo("Success", "Employee modified successfully")
            else:
                messagebox.showwarning("Warning", f"No employee found with ID {employee_id}")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No employees found")

    def display_employees(self):
        try:
            with open("employees.pickle", "rb") as file:
                employees = []
                while True:
                    try:
                        employee = pickle.load(file)
                        employees.append(employee)
                    except EOFError:
                        break
            # Display employee details
            if employees:
                display_window = tk.Toplevel(self.root)
                display_window.title("Employee Details")
                for i, employee in enumerate(employees):
                    tk.Label(display_window, text=f"Employee {i + 1}").grid(row=i, column=0, padx=5, pady=5, sticky='w')
                    tk.Label(display_window, text=f"Employee ID: {employee.employee_id}").grid(row=i, column=1, padx=5,
                                                                                               pady=5, sticky='w')
                    tk.Label(display_window, text=f"First Name: {employee.first_name}").grid(row=i, column=2, padx=5,
                                                                                             pady=5, sticky='w')
                    tk.Label(display_window, text=f"Last Name: {employee.last_name}").grid(row=i, column=3, padx=5,
                                                                                           pady=5, sticky='w')
                    tk.Label(display_window, text=f"Employee Type: {employee.employee_type}").grid(row=i, column=4,
                                                                                                   padx=5, pady=5,
                                                                                                   sticky='w')
                    tk.Label(display_window, text=f"Department: {employee.department}").grid(row=i, column=5, padx=5,
                                                                                             pady=5, sticky='w')
                    tk.Label(display_window, text=f"Job Title: {employee.job_title}").grid(row=i, column=6, padx=5,
                                                                                           pady=5, sticky='w')
                    tk.Label(display_window, text=f"Basic Salary: {employee.basic_salary}").grid(row=i, column=7,
                                                                                                 padx=5, pady=5,
                                                                                                 sticky='w')
                    tk.Label(display_window, text=f"Manager ID: {employee.manager_id}").grid(row=i, column=8, padx=5,
                                                                                             pady=5, sticky='w')
                    tk.Label(display_window, text=f"Age: {employee.age}").grid(row=i, column=9, padx=5, pady=5,
                                                                               sticky='w')
                    tk.Label(display_window, text=f"Date of Birth: {employee.date_of_birth}").grid(row=i, column=10,
                                                                                                   padx=5, pady=5,
                                                                                                   sticky='w')
                    tk.Label(display_window, text=f"Passport Details: {employee.passport_details}").grid(row=i,
                                                                                                         column=11,
                                                                                                         padx=5, pady=5,
                                                                                                         sticky='w')
            else:
                messagebox.showinfo("No Employees", "No employees found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No employees found")

    def open_event_management_window(self):
        event_window = tk.Toplevel(self.root)
        event_window.title("Event Management")

        # Add buttons
        tk.Button(event_window, text="Create Event", command=self.add_event).grid(row=2, column=0, pady=10)
        tk.Button(event_window, text="Delete Event", command=self.delete_event).grid(row=2, column=1, pady=10)
        tk.Button(event_window, text="Modify Event", command=self.modify_event).grid(row=2, column=2, pady=10)
        tk.Button(event_window, text="Display Events", command=self.display_events).grid(row=2, column=3, pady=10)

    def add_event(self):
        # Create a new Toplevel window for adding event details
        add_event_window = tk.Toplevel(self.root)
        add_event_window.title("Add Event")

        # Add labels and entry fields for each attribute of the event
        tk.Label(add_event_window, text="Event Type:").grid(row=0, column=0, padx=5, pady=5)
        self.event_type_entry = tk.Entry(add_event_window)
        self.event_type_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Theme:").grid(row=1, column=0, padx=5, pady=5)
        self.theme_entry = tk.Entry(add_event_window)
        self.theme_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Date:").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(add_event_window)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Time:").grid(row=3, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(add_event_window)
        self.time_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Duration:").grid(row=4, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(add_event_window)
        self.duration_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Venue Address:").grid(row=5, column=0, padx=5, pady=5)
        self.venue_address_entry = tk.Entry(add_event_window)
        self.venue_address_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Client ID:").grid(row=6, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(add_event_window)
        self.client_id_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Guest List:").grid(row=7, column=0, padx=5, pady=5)
        self.guest_list_entry = tk.Entry(add_event_window)
        self.guest_list_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Catering Company:").grid(row=8, column=0, padx=5, pady=5)
        self.catering_company_entry = tk.Entry(add_event_window)
        self.catering_company_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Cleaning Company:").grid(row=9, column=0, padx=5, pady=5)
        self.cleaning_company_entry = tk.Entry(add_event_window)
        self.cleaning_company_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Decorations Company:").grid(row=10, column=0, padx=5, pady=5)
        self.decorations_company_entry = tk.Entry(add_event_window)
        self.decorations_company_entry.grid(row=10, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Entertainment Company:").grid(row=11, column=0, padx=5, pady=5)
        self.entertainment_company_entry = tk.Entry(add_event_window)
        self.entertainment_company_entry.grid(row=11, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Furniture Supply Company:").grid(row=12, column=0, padx=5, pady=5)
        self.furniture_supply_company_entry = tk.Entry(add_event_window)
        self.furniture_supply_company_entry.grid(row=12, column=1, padx=5, pady=5)

        tk.Label(add_event_window, text="Invoice:").grid(row=13, column=0, padx=5, pady=5)
        self.invoice_entry = tk.Entry(add_event_window)
        self.invoice_entry.grid(row=13, column=1, padx=5, pady=5)

        # Create a button to submit the event details
        submit_button = tk.Button(add_event_window, text="Submit", command=self.submit_event)
        submit_button.grid(row=14, column=0, columnspan=2, padx=5, pady=10)

    def submit_event(self):
        # Retrieve the entered values from the entry fields
        event_type = self.event_type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        cleaning_company = self.cleaning_company_entry.get()
        decorations_company = self.decorations_company_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_supply_company = self.furniture_supply_company_entry.get()
        invoice = self.invoice_entry.get()

        # Create an Event object
        event = Event(event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                      catering_company, cleaning_company, decorations_company, entertainment_company,
                      furniture_supply_company, invoice)

        # Save Event object using Pickle
        with open("events.pickle", "ab") as file:
            pickle.dump(event, file)

        messagebox.showinfo("Success", "Event added successfully")

    def remove_event(self, event_id):
        try:
            with open("events.pickle", "rb") as file:
                events = []
                while True:
                    try:
                        event = pickle.load(file)
                        if event.event_id != event_id:
                            events.append(event)
                    except EOFError:
                        break
            with open("events.pickle", "wb") as file:
                for evt in events:
                    pickle.dump(evt, file)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No events found")

    def delete_event(self):
        # Create a new Toplevel window for deleting an event
        delete_event_window = tk.Toplevel(self.root)
        delete_event_window.title("Delete Event")

        # Add a label and entry field for entering the event ID
        tk.Label(delete_event_window, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        self.event_id_entry = tk.Entry(delete_event_window)
        self.event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to delete the event
        delete_button = tk.Button(delete_event_window, text="Delete", command=self.confirm_delete_event)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def confirm_delete_event(self):
        # Retrieve the entered event ID
        event_id = self.event_id_entry.get()

        # Confirm with the user before deletion
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete event with ID {event_id}?")

        if confirm:
            self.remove_event(event_id)
            messagebox.showinfo("Success", "Event deleted successfully")

    def modify_event(self):
        # Create a new Toplevel window for modifying an event
        modify_event_window = tk.Toplevel(self.root)
        modify_event_window.title("Modify Event")

        # Add labels and entry fields for the event ID and new details
        tk.Label(modify_event_window, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_event_id_entry = tk.Entry(modify_event_window)
        self.modify_event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add labels and entry fields for new event details
        tk.Label(modify_event_window, text="New Event Type:").grid(row=1, column=0, padx=5, pady=5)
        self.new_event_type_entry = tk.Entry(modify_event_window)
        self.new_event_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Theme:").grid(row=2, column=0, padx=5, pady=5)
        self.new_theme_entry = tk.Entry(modify_event_window)
        self.new_theme_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Date:").grid(row=3, column=0, padx=5, pady=5)
        self.new_date_entry = tk.Entry(modify_event_window)
        self.new_date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Time:").grid(row=4, column=0, padx=5, pady=5)
        self.new_time_entry = tk.Entry(modify_event_window)
        self.new_time_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Duration:").grid(row=5, column=0, padx=5, pady=5)
        self.new_duration_entry = tk.Entry(modify_event_window)
        self.new_duration_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Venue Address:").grid(row=6, column=0, padx=5, pady=5)
        self.new_venue_address_entry = tk.Entry(modify_event_window)
        self.new_venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Client ID:").grid(row=7, column=0, padx=5, pady=5)
        self.new_client_id_entry = tk.Entry(modify_event_window)
        self.new_client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Guest List:").grid(row=8, column=0, padx=5, pady=5)
        self.new_guest_list_entry = tk.Entry(modify_event_window)
        self.new_guest_list_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Catering Company:").grid(row=9, column=0, padx=5, pady=5)
        self.new_catering_company_entry = tk.Entry(modify_event_window)
        self.new_catering_company_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Cleaning Company:").grid(row=10, column=0, padx=5, pady=5)
        self.new_cleaning_company_entry = tk.Entry(modify_event_window)
        self.new_cleaning_company_entry.grid(row=10, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Decorations Company:").grid(row=11, column=0, padx=5, pady=5)
        self.new_decorations_company_entry = tk.Entry(modify_event_window)
        self.new_decorations_company_entry.grid(row=11, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Entertainment Company:").grid(row=12, column=0, padx=5, pady=5)
        self.new_entertainment_company_entry = tk.Entry(modify_event_window)
        self.new_entertainment_company_entry.grid(row=12, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Furniture Supply Company:").grid(row=13, column=0, padx=5, pady=5)
        self.new_furniture_supply_company_entry = tk.Entry(modify_event_window)
        self.new_furniture_supply_company_entry.grid(row=13, column=1, padx=5, pady=5)

        tk.Label(modify_event_window, text="New Invoice:").grid(row=14, column=0, padx=5, pady=5)
        self.new_invoice_entry = tk.Entry(modify_event_window)
        self.new_invoice_entry.grid(row=14, column=1, padx=5, pady=5)

        # Create a button to modify the event details
        modify_button = tk.Button(modify_event_window, text="Modify", command=self.confirm_modify_event)
        modify_button.grid(row=15, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_event(self):
        # Retrieve the entered event ID and new details
        event_id = self.modify_event_id_entry.get()
        new_event_type = self.new_event_type_entry.get()
        new_theme = self.new_theme_entry.get()
        new_date = self.new_date_entry.get()
        new_time = self.new_time_entry.get()
        new_duration = self.new_duration_entry.get()
        new_venue_address = self.new_venue_address_entry.get()
        new_client_id = self.new_client_id_entry.get()
        new_guest_list = self.new_guest_list_entry.get()
        new_catering_company = self.new_catering_company_entry.get()
        new_cleaning_company = self.new_cleaning_company_entry.get()
        new_decorations_company = self.new_decorations_company_entry.get()
        new_entertainment_company = self.new_entertainment_company_entry.get()
        new_furniture_supply_company = self.new_furniture_supply_company_entry.get()
        new_invoice = self.new_invoice_entry.get()

        event = Event(new_event_type, new_theme, new_date, new_time, new_duration ,new_venue_address, new_client_id, new_guest_list, new_catering_company, new_cleaning_company, new_decorations_company, new_entertainment_company, new_furniture_supply_company, new_invoice)

        self.remove_event(event_id)
        event.set_event_id(event_id)

        # Save Event object using Pickle
        with open("events.pickle", "ab") as file:
            pickle.dump(event, file)

        messagebox.showinfo("Success", "Event modified successfully")

    def display_events(self):
        try:
            with open("events.pickle", "rb") as file:
                events = []
                while True:
                    try:
                        event = pickle.load(file)
                        events.append(event)
                    except EOFError:
                        break
            # Display event details
            if events:
                display_window = tk.Toplevel(self.root)
                display_window.title("Event Details")
                for i, event in enumerate(events):
                    tk.Label(display_window, text=f"Event {i + 1}").grid(row=i, column=0, padx=5, pady=5, sticky='w')
                    tk.Label(display_window, text=f"Event ID: {event.event_id}").grid(row=i, column=1, padx=5, pady=5,
                                                                                      sticky='w')
                    tk.Label(display_window, text=f"Event Type: {event.event_type}").grid(row=i, column=2, padx=5,
                                                                                          pady=5, sticky='w')
                    tk.Label(display_window, text=f"Theme: {event.theme}").grid(row=i, column=3, padx=5, pady=5,
                                                                                sticky='w')
                    tk.Label(display_window, text=f"Date: {event.date}").grid(row=i, column=4, padx=5, pady=5,
                                                                              sticky='w')
                    tk.Label(display_window, text=f"Time: {event.time}").grid(row=i, column=5, padx=5, pady=5,
                                                                              sticky='w')
                    tk.Label(display_window, text=f"Duration: {event.duration}").grid(row=i, column=6, padx=5, pady=5,
                                                                                      sticky='w')
                    tk.Label(display_window, text=f"Venue Address: {event.venue_address}").grid(row=i, column=7, padx=5,
                                                                                                pady=5, sticky='w')
                    tk.Label(display_window, text=f"Client ID: {event.client_id}").grid(row=i, column=8, padx=5, pady=5,
                                                                                        sticky='w')
                    tk.Label(display_window, text=f"Guest List: {event.guest_list}").grid(row=i, column=9, padx=5,
                                                                                          pady=5, sticky='w')
                    tk.Label(display_window, text=f"Catering Company: {event.catering_company}").grid(row=i, column=10,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky='w')
                    tk.Label(display_window, text=f"Cleaning Company: {event.cleaning_company}").grid(row=i, column=11,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky='w')
                    tk.Label(display_window, text=f"Decorations Company: {event.decorations_company}").grid(row=i,
                                                                                                            column=12,
                                                                                                            padx=5,
                                                                                                            pady=5,
                                                                                                            sticky='w')
                    tk.Label(display_window, text=f"Entertainment Company: {event.entertainment_company}").grid(row=i,
                                                                                                                column=13,
                                                                                                                padx=5,
                                                                                                                pady=5,
                                                                                                                sticky='w')
                    tk.Label(display_window, text=f"Furniture Supply Company: {event.furniture_supply_company}").grid(
                        row=i, column=14, padx=5, pady=5, sticky='w')
                    tk.Label(display_window, text=f"Invoice: {event.invoice}").grid(row=i, column=15, padx=5, pady=5,
                                                                                    sticky='w')
            else:
                messagebox.showinfo("No Events", "No events found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No events found")

    def open_client_management_window(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Client Management")

        # Add widgets for managing clients
        tk.Button(client_window, text="Add Client", command=self.add_client).pack(pady=10)
        tk.Button(client_window, text="Delete Client", command=self.delete_client).pack(pady=10)
        tk.Button(client_window, text="Modify Client", command=self.modify_client).pack(pady=10)
        tk.Button(client_window, text="Display Clients", command=self.display_clients).pack(pady=10)

    def add_client(self):
        # Create a new Toplevel window for adding a client details
        add_client_window = tk.Toplevel(self.root)
        add_client_window.title("Add Client")

        # Add labels and entry fields for each attribute of the client
        tk.Label(add_client_window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        self.client_first_name_entry = tk.Entry(add_client_window)
        self.client_first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_client_window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        self.client_last_name_entry = tk.Entry(add_client_window)
        self.client_last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_client_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.client_address_entry = tk.Entry(add_client_window)
        self.client_address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_client_window, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.client_contact_details_entry = tk.Entry(add_client_window)
        self.client_contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_client_window, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
        self.client_budget_entry = tk.Entry(add_client_window)
        self.client_budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a button to submit the client details
        submit_button = tk.Button(add_client_window, text="Submit", command=self.submit_client)
        submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def submit_client(self):
        # Retrieve the entered values from the entry fields
        first_name = self.client_first_name_entry.get()
        last_name = self.client_last_name_entry.get()
        address = self.client_address_entry.get()
        contact_details = self.client_contact_details_entry.get()
        budget = self.client_budget_entry.get()

        # Create a new Client object
        client = Client(first_name, last_name, address, contact_details, budget)

        # Save Client object using Pickle
        with open("clients.pickle", "ab") as file:
            pickle.dump(client, file)

        # Show success message
        messagebox.showinfo("Success", "Client added successfully")

    def remove_client(self, client_id):
        try:
            with open("clients.pickle", "rb") as file:
                clients = []
                while True:
                    try:
                        client = pickle.load(file)
                        if client.client_id != client_id:
                            clients.append(client)
                    except EOFError:
                        break
            with open("clients.pickle", "wb") as file:
                for clt in clients:
                    pickle.dump(clt, file)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No clients found")

    def delete_client(self):
        # Create a new Toplevel window for deleting a client
        delete_client_window = tk.Toplevel(self.root)
        delete_client_window.title("Delete Client")

        # Add a label and entry field for entering the client ID
        tk.Label(delete_client_window, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(delete_client_window)
        self.client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to delete the client
        delete_button = tk.Button(delete_client_window, text="Delete", command=self.confirm_delete_client)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def confirm_delete_client(self):
        # Retrieve the entered client ID
        client_id = self.client_id_entry.get()

        # Confirm with the user before deletion
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete client with ID {client_id}?")

        if confirm:
            self.remove_client(client_id)
            messagebox.showinfo("Success", "Client deleted successfully")

    def modify_client(self):
        # Create a new Toplevel window for modifying a client details
        modify_client_window = tk.Toplevel(self.root)
        modify_client_window.title("Modify Client")

        # Add labels and entry fields for each attribute of the client (new details)
        tk.Label(modify_client_window, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_client_id_entry = tk.Entry(modify_client_window)
        self.modify_client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(modify_client_window, text="First Name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_client_first_name_entry = tk.Entry(modify_client_window)
        self.new_client_first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_client_window, text="Last Name:").grid(row=2, column=0, padx=5, pady=5)
        self.new_client_last_name_entry = tk.Entry(modify_client_window)
        self.new_client_last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_client_window, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.new_client_address_entry = tk.Entry(modify_client_window)
        self.new_client_address_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_client_window, text="Contact Details:").grid(row=4, column=0, padx=5, pady=5)
        self.new_client_contact_details_entry = tk.Entry(modify_client_window)
        self.new_client_contact_details_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(modify_client_window, text="Budget:").grid(row=5, column=0, padx=5, pady=5)
        self.new_client_budget_entry = tk.Entry(modify_client_window)
        self.new_client_budget_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create a button to submit the client details
        modify_button = tk.Button(modify_client_window, text="Modify", command=self.confirm_modify_client)
        modify_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_client(self):
        # Retrieve the entered client ID and new details
        client_id = self.modify_client_id_entry.get()
        new_first_name = self.new_client_first_name_entry.get()
        new_last_name = self.new_client_last_name_entry.get()
        new_address = self.new_client_address_entry.get()
        new_contact_details = self.new_client_contact_details_entry.get()
        new_budget = self.new_client_budget_entry.get()

        client = Client(new_first_name, new_last_name, new_address, new_contact_details ,new_budget)

        self.remove_client(client_id)
        client.set_client_id(client_id)

        # Save Client object using Pickle
        with open("clients.pickle", "ab") as file:
            pickle.dump(client, file)

        messagebox.showinfo("Success", "Client modified successfully")

    def display_clients(self):
        try:
            with open("clients.pickle", "rb") as file:
                clients = []
                while True:
                    try:
                        client = pickle.load(file)
                        clients.append(client)
                    except EOFError:
                        break

            # Display client details
            if clients:
                display_window = tk.Toplevel(self.root)
                display_window.title("Client Details")
                for i, client in enumerate(clients):
                    tk.Label(display_window, text=f"Client {i + 1}").grid(row=i, column=0, padx=5, pady=5, sticky='w')
                    tk.Label(display_window, text=f"Client ID: {client.client_id}").grid(row=i, column=1, padx=5,
                                                                                         pady=5,
                                                                                         sticky='w')
                    tk.Label(display_window, text=f"First Name: {client.first_name}").grid(row=i, column=2, padx=5,
                                                                                           pady=5,
                                                                                           sticky='w')
                    tk.Label(display_window, text=f"Last Name: {client.last_name}").grid(row=i, column=3, padx=5,
                                                                                         pady=5,
                                                                                         sticky='w')
                    tk.Label(display_window, text=f"Address: {client.address}").grid(row=i, column=4, padx=5, pady=5,
                                                                                     sticky='w')
                    tk.Label(display_window, text=f"Contact Details: {client.contact_details}").grid(row=i, column=5,
                                                                                                     padx=5,
                                                                                                     pady=5, sticky='w')
                    tk.Label(display_window, text=f"Budget: {client.budget}").grid(row=i, column=6, padx=5, pady=5,
                                                                                   sticky='w')
            else:
                messagebox.showinfo("No Clients", "No clients found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No clients found")

    def open_guest_management_window(self):
        guest_window = tk.Toplevel(self.root)
        guest_window.title("Guest Management")

        # Add buttons
        tk.Button(guest_window, text="Create Guest", command=self.add_guest).grid(row=2, column=0, pady=10)
        tk.Button(guest_window, text="Delete Guest", command=self.delete_guest).grid(row=2, column=1, pady=10)
        tk.Button(guest_window, text="Modify Guest", command=self.modify_guest).grid(row=2, column=2, pady=10)
        tk.Button(guest_window, text="Display Guest", command=self.display_guests).grid(row=2, column=3, pady=10)

    def add_guest(self):
        # Create a new Toplevel window for adding a guest details
        add_guest_window = tk.Toplevel(self.root)
        add_guest_window.title("Add Guest")

        # Add labels and entry fields for each attribute of the guest
        tk.Label(add_guest_window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        self.guest_first_name_entry = tk.Entry(add_guest_window)
        self.guest_first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_guest_window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        self.guest_last_name_entry = tk.Entry(add_guest_window)
        self.guest_last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_guest_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.guest_address_entry = tk.Entry(add_guest_window)
        self.guest_address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_guest_window, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.guest_contact_details_entry = tk.Entry(add_guest_window)
        self.guest_contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create a button to submit the guest details
        submit_button = tk.Button(add_guest_window, text="Submit", command=self.submit_guest)
        submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def submit_guest(self):
        # Retrieve the entered values from the entry fields
        first_name = self.guest_first_name_entry.get()
        last_name = self.guest_last_name_entry.get()
        address = self.guest_address_entry.get()
        contact_details = self.guest_contact_details_entry.get()

        # Create a new guest object
        guest = Guest(first_name, last_name, address, contact_details)

        # Save guest object using Pickle
        with open("guests.pickle", "ab") as file:
            pickle.dump(guest, file)

        # Show success message
        messagebox.showinfo("Success", "Guest added successfully")

    def remove_guest(self, guest_id):
        try:
            with open("guests.pickle", "rb") as file:
                guests = []
                while True:
                    try:
                        guest = pickle.load(file)
                        if guest.guest_id != guest_id:
                            guests.append(guest)
                    except EOFError:
                        break
            with open("guests.pickle", "wb") as file:
                for gst in guests:
                    pickle.dump(gst, file)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No guests found")

    def delete_guest(self):
        # Create a new Toplevel window for deleting a guest
        delete_guest_window = tk.Toplevel(self.root)
        delete_guest_window.title("Delete Guest")

        # Add a label and entry field for entering the guest ID
        tk.Label(delete_guest_window, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        self.guest_id_entry = tk.Entry(delete_guest_window)
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to delete the guest
        delete_button = tk.Button(delete_guest_window, text="Delete", command=self.confirm_delete_guest)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def confirm_delete_guest(self):
        # Retrieve the entered guest ID
        guest_id = self.guest_id_entry.get()

        # Confirm with the user before deletion
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete guest with ID {guest_id}?")

        if confirm:
            self.remove_guest(guest_id)
            messagebox.showinfo("Success", "Guest deleted successfully")

    def modify_guest(self):
        # Create a new Toplevel window for modifying a guest details
        modify_guest_window = tk.Toplevel(self.root)
        modify_guest_window.title("Modify Guest")

        # Add labels and entry fields for each attribute of the guest (new details)
        tk.Label(modify_guest_window, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_guest_id_entry = tk.Entry(modify_guest_window)
        self.modify_guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(modify_guest_window, text="First Name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_guest_first_name_entry = tk.Entry(modify_guest_window)
        self.new_guest_first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_guest_window, text="Last Name:").grid(row=2, column=0, padx=5, pady=5)
        self.new_guest_last_name_entry = tk.Entry(modify_guest_window)
        self.new_guest_last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_guest_window, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.new_guest_address_entry = tk.Entry(modify_guest_window)
        self.new_guest_address_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_guest_window, text="Contact Details:").grid(row=4, column=0, padx=5, pady=5)
        self.new_guest_contact_details_entry = tk.Entry(modify_guest_window)
        self.new_guest_contact_details_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a button to submit the guest details
        modify_button = tk.Button(modify_guest_window, text="Modify", command=self.confirm_modify_guest)
        modify_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_guest(self):
        # Retrieve the entered guest ID and new details
        guest_id = self.modify_guest_id_entry.get()
        new_first_name = self.new_guest_first_name_entry.get()
        new_last_name = self.new_guest_last_name_entry.get()
        new_address = self.new_guest_address_entry.get()
        new_contact_details = self.new_guest_contact_details_entry.get()

        guest = Guest(new_first_name, new_last_name, new_address, new_contact_details)

        self.remove_guest(guest_id)
        guest.set_guest_id(guest_id)

        # Save Guest object using Pickle
        with open("guests.pickle", "ab") as file:
            pickle.dump(guest, file)

        messagebox.showinfo("Success", "Guest modified successfully")

    def display_guests(self):
        try:
            with open("guests.pickle", "rb") as file:
                guests = []
                while True:
                    try:
                        guest = pickle.load(file)
                        guests.append(guest)
                    except EOFError:
                        break

            # Display guest details
            if guests:
                display_window = tk.Toplevel(self.root)
                display_window.title("Guest Details")
                for i, guest in enumerate(guests):
                    tk.Label(display_window, text=f"Guest {i + 1}").grid(row=i, column=0, padx=5, pady=5, sticky='w')
                    tk.Label(display_window, text=f"Guest ID: {guest.guest_id}").grid(row=i, column=1, padx=5,
                                                                                         pady=5,
                                                                                         sticky='w')
                    tk.Label(display_window, text=f"First Name: {guest.first_name}").grid(row=i, column=2, padx=5,
                                                                                           pady=5,
                                                                                           sticky='w')
                    tk.Label(display_window, text=f"Last Name: {guest.last_name}").grid(row=i, column=3, padx=5,
                                                                                         pady=5,
                                                                                         sticky='w')
                    tk.Label(display_window, text=f"Address: {guest.address}").grid(row=i, column=4, padx=5, pady=5,
                                                                                     sticky='w')
                    tk.Label(display_window, text=f"Contact Details: {guest.contact_details}").grid(row=i, column=5,
                                                                                                     padx=5,
                                                                                                     pady=5, sticky='w')

            else:
                messagebox.showinfo("No Guests", "No guests found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No guests found")


    def open_supplier_management_window(self):
        supplier_window = tk.Toplevel(self.root)
        supplier_window.title("Supplier Management")

        # Add buttons
        tk.Button(supplier_window, text="Create Supplier", command=self.add_supplier).grid(row=2, column=0, pady=10)
        tk.Button(supplier_window, text="Delete Supplier", command=self.delete_supplier).grid(row=2, column=1, pady=10)
        tk.Button(supplier_window, text="Modify Supplier", command=self.modify_supplier).grid(row=2, column=2, pady=10)
        tk.Button(supplier_window, text="Display Supplier", command=self.display_supplier).grid(row=2, column=3, pady=10)

    def add_supplier(self):
        add_supplier_window = tk.Toplevel(self.root)
        add_supplier_window.title("Supplier Options")

        # Add options
        tk.Button(add_supplier_window, text="Create Caterer", command=self.add_caterer).grid(row=2, column=0, pady=10)
        tk.Button(add_supplier_window, text="Create Cleaning Company", command=self.add_cleaner).grid(row=2, column=1, pady=10)
        tk.Button(add_supplier_window, text="Create Furniture Company", command=self.add_furniture).grid(row=2, column=2, pady=10)
        tk.Button(add_supplier_window, text="Create Decoration Company", command=self.add_decoration).grid(row=2, column=3,
                                                                                                pady=10)

    def add_caterer(self):
        # Create a new Toplevel window for adding a caterer details
        add_caterer_window = tk.Toplevel(self.root)
        add_caterer_window.title("Add Caterer")

        # Add labels and entry fields for each attribute of the caterer
        tk.Label(add_caterer_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.caterer_name_entry = tk.Entry(add_caterer_window)
        self.caterer_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_caterer_window, text="Address:").grid(row=1, column=0, padx=5, pady=5)
        self.caterer_address_entry = tk.Entry(add_caterer_window)
        self.caterer_address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_caterer_window, text="Contact:").grid(row=2, column=0, padx=5, pady=5)
        self.caterer_contact_entry = tk.Entry(add_caterer_window)
        self.caterer_contact_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_caterer_window, text="Menu:").grid(row=3, column=0, padx=5, pady=5)
        self.caterer_menu_entry = tk.Entry(add_caterer_window)
        self.caterer_menu_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_caterer_window, text="Maximum number of guests:").grid(row=4, column=0, padx=5, pady=5)
        self.caterer_max_entry = tk.Entry(add_caterer_window)
        self.caterer_max_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_caterer_window, text="Minimum number of guests:").grid(row=5, column=0, padx=5, pady=5)
        self.caterer_min_entry = tk.Entry(add_caterer_window)
        self.caterer_min_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create a button to submit the cleaner details
        submit_button = tk.Button(add_caterer_window, text="Submit", command=self.submit_caterer)
        submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def submit_caterer(self):
        # Retrieve the entered values from the entry fields
        name = self.caterer_name_entry.get()
        address = self.caterer_address_entry.get()
        contact = self.caterer_contact_entry.get()
        menu = self.caterer_menu_entry.get()
        max = self.caterer_max_entry.get()
        min = self.caterer_min_entry.get()


        # Create a new caterer object
        caterer = Caterer(name, address, contact, menu, max, min)

        # Save caterer object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(caterer, file)

        # Show success message
        messagebox.showinfo("Success", "Caterer added successfully")

    def add_cleaner(self):
        # Create a new Toplevel window for adding a cleaner details
        add_cleaner_window = tk.Toplevel(self.root)
        add_cleaner_window.title("Add Cleaner")

        # Add labels and entry fields for each attribute of the cleaner
        tk.Label(add_cleaner_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.cleaner_name_entry = tk.Entry(add_cleaner_window)
        self.cleaner_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_cleaner_window, text="Address:").grid(row=1, column=0, padx=5, pady=5)
        self.cleaner_address_entry = tk.Entry(add_cleaner_window)
        self.cleaner_address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_cleaner_window, text="Contact:").grid(row=2, column=0, padx=5, pady=5)
        self.cleaner_contact_entry = tk.Entry(add_cleaner_window)
        self.cleaner_contact_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_cleaner_window, text="Services:").grid(row=3, column=0, padx=5, pady=5)
        self.cleaner_service_entry = tk.Entry(add_cleaner_window)
        self.cleaner_service_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create a button to submit the cleaner details
        submit_button = tk.Button(add_cleaner_window, text="Submit", command=self.submit_cleaner)
        submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def submit_cleaner(self):
        # Retrieve the entered values from the entry fields
        name = self.cleaner_name_entry.get()
        address = self.cleaner_address_entry.get()
        contact = self.cleaner_contact_entry.get()
        service = self.cleaner_service_entry.get()


        # Create a new cleaner object
        cleaner = Cleaner(name, address, contact, service)

        # Save cleaner object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(cleaner, file)

        # Show success message
        messagebox.showinfo("Success", "Cleaner added successfully")

    def add_furniture(self):
        # Create a new Toplevel window for adding furniture details
        add_furniture_window = tk.Toplevel(self.root)
        add_furniture_window.title("Add Furniture Company")

        # Add labels and entry fields for each attribute of the furniture
        tk.Label(add_furniture_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.furniture_name_entry = tk.Entry(add_furniture_window)
        self.furniture_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_furniture_window, text="Address:").grid(row=1, column=0, padx=5, pady=5)
        self.furniture_address_entry = tk.Entry(add_furniture_window)
        self.furniture_address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_furniture_window, text="Contact:").grid(row=2, column=0, padx=5, pady=5)
        self.furniture_contact_entry = tk.Entry(add_furniture_window)
        self.furniture_contact_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_furniture_window, text="Available Items:").grid(row=3, column=0, padx=5, pady=5)
        self.furniture_items_entry = tk.Entry(add_furniture_window)
        self.furniture_items_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create a button to submit the company details
        submit_button = tk.Button(add_furniture_window, text="Submit", command=self.submit_furniture)
        submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def submit_furniture(self):
        # Retrieve the entered values from the entry fields
        name = self.furniture_name_entry.get()
        address = self.furniture_address_entry.get()
        contact = self.furniture_contact_entry.get()
        items = self.furniture_items_entry.get()

        # Create a new furniture company object
        furniture = FurnitureSupplier(name, address, contact, items)

        # Save furniture object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(furniture, file)

        # Show success message
        messagebox.showinfo("Success", "Furniture Company added successfully")

    def add_decoration(self):
        # Create a new Toplevel window for adding decoration details
        add_decoration_window = tk.Toplevel(self.root)
        add_decoration_window.title("Add Decoration Company")

        # Add labels and entry fields for each attribute of the decoration
        tk.Label(add_decoration_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.decoration_name_entry = tk.Entry(add_decoration_window)
        self.decoration_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_decoration_window, text="Address:").grid(row=1, column=0, padx=5, pady=5)
        self.decoration_address_entry = tk.Entry(add_decoration_window)
        self.decoration_address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_decoration_window, text="Contact:").grid(row=2, column=0, padx=5, pady=5)
        self.decoration_contact_entry = tk.Entry(add_decoration_window)
        self.decoration_contact_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_decoration_window, text="Available Items:").grid(row=3, column=0, padx=5, pady=5)
        self.decoration_items_entry = tk.Entry(add_decoration_window)
        self.decoration_items_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create a button to submit the company details
        submit_button = tk.Button(add_decoration_window, text="Submit", command=self.submit_decoration)
        submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def submit_decoration(self):
        # Retrieve the entered values from the entry fields
        name = self.decoration_name_entry.get()
        address = self.decoration_address_entry.get()
        contact = self.decoration_contact_entry.get()
        items = self.decoration_items_entry.get()

        # Create a new decoration company object
        decoration = DecorationSupplier(name, address, contact, items)

        # Save decoration object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(decoration, file)

        # Show success message
        messagebox.showinfo("Success", "Decoration Company added successfully")

    def remove_supplier(self, supplier_id):
        try:
            with open("suppliers.pickle", "rb") as file:
                suppliers = []
                while True:
                    try:
                        supplier = pickle.load(file)
                        if supplier.supplier_id != supplier_id:
                            suppliers.append(supplier)
                    except EOFError:
                        break
            with open("suppliers.pickle", "wb") as file:
                for spl in suppliers:
                    pickle.dump(spl, file)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No Suppliers found")

    def delete_supplier(self):
        # Create a new Toplevel window for deleting a supplier
        delete_supplier_window = tk.Toplevel(self.root)
        delete_supplier_window.title("Delete Suppler")

        # Add a label and entry field for entering the supplier ID
        tk.Label(delete_supplier_window, text="Supplier ID:").grid(row=0, column=0, padx=5, pady=5)
        self.supplier_id_entry = tk.Entry(delete_supplier_window)
        self.supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to delete the supplier
        delete_button = tk.Button(delete_supplier_window, text="Delete", command=self.confirm_delete_supplier)
        delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def confirm_delete_supplier(self):
        # Retrieve the entered supplier ID
        supplier_id = self.supplier_id_entry.get()

        # Confirm with the user before deletion
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete supplier with ID {supplier_id}?")

        if confirm:
            self.remove_guest(supplier_id)
            messagebox.showinfo("Success", "Supplier deleted successfully")

    def modify_supplier(self):
        # Create a new Toplevel window for modifying a supplier details
        modify_supplier_window = tk.Toplevel(self.root)
        modify_supplier_window.title("Choose the supplier you want to modify")

        # Add options
        tk.Button(modify_supplier_window, text="Caterer", command=self.modify_caterer).grid(row=2, column=0, pady=10)
        tk.Button(modify_supplier_window, text="Cleaning Company", command=self.modify_cleaner).grid(row=2, column=1, pady=10)
        tk.Button(modify_supplier_window, text="Furniture Company", command=self.modify_furniture).grid(row=2,column=2,pady=10)
        tk.Button(modify_supplier_window, text="Decoration Company", command=self.modify_decoration).grid(row=2,column=3,pady=10)

    def modify_caterer(self):
        # Create a new Toplevel window for modifying a caterer details
        modify_caterer_window = tk.Toplevel(self.root)
        modify_caterer_window.title("Modify Caterer")

        # Add labels and entry fields for each attribute of the caterer (new details)
        tk.Label(modify_caterer_window, text="Caterer ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_caterer_id = tk.Entry(modify_caterer_window)
        self.modify_caterer_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(modify_caterer_window, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_caterer_name_entry = tk.Entry(modify_caterer_window)
        self.new_caterer_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_caterer_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.new_caterer_address_entry = tk.Entry(modify_caterer_window)
        self.new_caterer_address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_caterer_window, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.new_caterer_contact_entry = tk.Entry(modify_caterer_window)
        self.new_caterer_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_caterer_window, text="Menu:").grid(row=4, column=0, padx=5, pady=5)
        self.new_caterer_menu_entry = tk.Entry(modify_caterer_window)
        self.new_caterer_menu_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(modify_caterer_window, text="Maximum number of guests:").grid(row=5, column=0, padx=5, pady=5)
        self.new_caterer_max_entry = tk.Entry(modify_caterer_window)
        self.new_caterer_max_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(modify_caterer_window, text="Minimum number of guests:").grid(row=6, column=0, padx=5, pady=5)
        self.new_caterer_min_entry = tk.Entry(modify_caterer_window)
        self.new_caterer_min_entry.grid(row=6, column=1, padx=5, pady=5)

        # Create a button to submit the caterer details
        modify_button = tk.Button(modify_caterer_window, text="Modify", command=self.confirm_modify_caterer)
        modify_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_caterer(self):
        # Retrieve the entered caterer ID and new details
        caterer_id = self.modify_caterer_id.get()
        new_name = self.new_caterer_name_entry.get()
        new_address = self.new_caterer_address_entry.get()
        new_contact = self.new_caterer_contact_entry.get()
        new_menu = self.new_caterer_menu_entry.get()
        new_max = self.new_caterer_max_entry.get()
        new_min = self.new_caterer_min_entry.get()

        caterer = Caterer(new_name, new_address, new_contact, new_menu, new_min, new_max)

        self.remove_supplier(caterer_id)
        caterer.set_supplier_id(caterer_id)

        # Save caterer object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(caterer, file)

        messagebox.showinfo("Success", "Caterer modified successfully")

    def modify_cleaner(self):
        # Create a new Toplevel window for modifying a cleaner details
        modify_cleaner_window = tk.Toplevel(self.root)
        modify_cleaner_window.title("Modify Cleaner")

        # Add labels and entry fields for each attribute of the cleaner (new details)
        tk.Label(modify_cleaner_window, text="Cleaner ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_cleaner_id = tk.Entry(modify_cleaner_window)
        self.modify_cleaner_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(modify_cleaner_window, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_cleaner_name_entry = tk.Entry(modify_cleaner_window)
        self.new_cleaner_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_cleaner_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.new_cleaner_address_entry = tk.Entry(modify_cleaner_window)
        self.new_cleaner_address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_cleaner_window, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.new_cleaner_contact_entry = tk.Entry(modify_cleaner_window)
        self.new_cleaner_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_cleaner_window, text="Services:").grid(row=4, column=0, padx=5, pady=5)
        self.new_cleaner_service_entry = tk.Entry(modify_cleaner_window)
        self.new_cleaner_service_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a button to submit the cleaner details
        modify_button = tk.Button(modify_cleaner_window, text="Modify", command=self.confirm_modify_cleaner)
        modify_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_cleaner(self):
        # Retrieve the entered cleaner ID and new details
        cleaner_id = self.modify_cleaner_id.get()
        new_name = self.new_cleaner_name_entry.get()
        new_address = self.new_cleaner_address_entry.get()
        new_contact = self.new_cleaner_contact_entry.get()
        new_menu = self.new_cleaner_service_entry.get()

        cleaner = Cleaner(new_name, new_address, new_contact, new_menu)

        self.remove_supplier(cleaner_id)
        cleaner.set_supplier_id(cleaner_id)

        # Save cleaner object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(cleaner, file)

        messagebox.showinfo("Success", "Cleaner modified successfully")

    def modify_furniture(self):
        # Create a new Toplevel window for modifying furniture details
        modify_furniture_window = tk.Toplevel(self.root)
        modify_furniture_window.title("Modify Furniture Company")

        # Add labels and entry fields for each attribute of the furniture company (new details)
        tk.Label(modify_furniture_window, text="Furniture ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_furniture_id = tk.Entry(modify_furniture_window)
        self.modify_furniture_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(modify_furniture_window, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_furniture_name_entry = tk.Entry(modify_furniture_window)
        self.new_furniture_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_furniture_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.new_furniture_address_entry = tk.Entry(modify_furniture_window)
        self.new_furniture_address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_furniture_window, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.new_furniture_contact_entry = tk.Entry(modify_furniture_window)
        self.new_furniture_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_furniture_window, text="Available items:").grid(row=4, column=0, padx=5, pady=5)
        self.new_furniture_items_entry = tk.Entry(modify_furniture_window)
        self.new_furniture_items_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a button to submit the company details
        modify_button = tk.Button(modify_furniture_window, text="Modify", command=self.confirm_modify_furniture)
        modify_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_furniture(self):
        # Retrieve the entered furniture ID and new details
        furniture_id = self.modify_furniture_id.get()
        new_name = self.new_furniture_name_entry.get()
        new_address = self.new_furniture_address_entry.get()
        new_contact = self.new_furniture_contact_entry.get()
        new_items = self.new_furniture_items_entry.get()

        furniture = FurnitureSupplier(new_name, new_address, new_contact, new_items)

        self.remove_supplier(furniture_id)
        furniture.set_supplier_id(furniture_id)

        # Save furniture object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(furniture, file)

        messagebox.showinfo("Success", "Furniture modified successfully")

    def modify_decoration(self):
        # Create a new Toplevel window for modifying decoration details
        modify_decoration_window = tk.Toplevel(self.root)
        modify_decoration_window.title("Modify Decoration Company")

        # Add labels and entry fields for each attribute of the decoration company (new details)
        tk.Label(modify_decoration_window, text="Decoration ID:").grid(row=0, column=0, padx=5, pady=5)
        self.modify_decoration_id = tk.Entry(modify_decoration_window)
        self.modify_decoration_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(modify_decoration_window, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.new_decoration_name_entry = tk.Entry(modify_decoration_window)
        self.new_decoration_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(modify_decoration_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.new_decoration_address_entry = tk.Entry(modify_decoration_window)
        self.new_decoration_address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(modify_decoration_window, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.new_decoration_contact_entry = tk.Entry(modify_decoration_window)
        self.new_decoration_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(modify_decoration_window, text="Available items:").grid(row=4, column=0, padx=5, pady=5)
        self.new_decoration_items_entry = tk.Entry(modify_decoration_window)
        self.new_decoration_items_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a button to submit the company details
        modify_button = tk.Button(modify_decoration_window, text="Modify", command=self.confirm_modify_decoration)
        modify_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def confirm_modify_decoration(self):
        # Retrieve the entered decoration ID and new details
        decoration_id = self.modify_decoration_id.get()
        new_name = self.new_decoration_name_entry.get()
        new_address = self.new_decoration_address_entry.get()
        new_contact = self.new_decoration_contact_entry.get()
        new_items = self.new_decoration_items_entry.get()

        decoration = DecorationSupplier(new_name, new_address, new_contact, new_items)

        self.remove_supplier(decoration_id)
        decoration.set_supplier_id(decoration_id)

        # Save furniture object using Pickle
        with open("suppliers.pickle", "ab") as file:
            pickle.dump(decoration, file)

        messagebox.showinfo("Success", "Decoration Company modified successfully")

    def display_supplier(self):
        try:
            with open("suppliers.pickle", "rb") as file:
                suppliers = []
                while True:
                    try:
                        supplier = pickle.load(file)
                        suppliers.append(supplier)
                    except EOFError:
                        break

            # Display supplier details
            if suppliers:
                display_window = tk.Toplevel(self.root)
                display_window.title("Supplier Details")
                for i, supplier in enumerate(suppliers):
                    tk.Label(display_window, text=f"Supplier {i + 1}").grid(row=i, column=0, padx=5, pady=5, sticky='w')
                    tk.Label(display_window, text=f"Supplier ID: {supplier.supplier_id}").grid(row=i, column=1, padx=5,
                                                                                         pady=5,
                                                                                         sticky='w')
                    tk.Label(display_window, text=f"Supplier Name: {supplier.name}").grid(row=i, column=2, padx=5,
                                                                                           pady=5,
                                                                                           sticky='w')
                    tk.Label(display_window, text=f"Address: {supplier.address}").grid(row=i, column=3, padx=5,
                                                                                         pady=5,
                                                                                         sticky='w')
                    tk.Label(display_window, text=f"Contact: {supplier.contact}").grid(row=i, column=4, padx=5, pady=5,
                                                                                     sticky='w')

            else:
                messagebox.showinfo("No Suppliers", "No suppliers found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No suppliers found")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompanyManagementApp(root)
    root.mainloop()