import os


# Parent Class
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display(self):
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)


# Child Class
class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, salary, bonus):
        super().__init__(employee_id, name, salary)
        self.bonus = bonus

    # Method overriding
    def calculate_salary(self):
        return self.salary + self.bonus

    def display(self):
        super().display()
        print("Bonus       :", self.bonus)
        print("Total Salary:", self.calculate_salary())


class EmployeeManagementSystem:

    FILE_NAME = "employees.txt"

    def add_employee(self):
        try:
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Salary: "))
            bonus = float(input("Enter Bonus: "))

            employee = PermanentEmployee(
                employee_id,
                name,
                salary,
                bonus
            )

            with open(self.FILE_NAME, "a") as file:
                file.write(
                    f"{employee.employee_id},"
                    f"{employee.name},"
                    f"{employee.salary},"
                    f"{employee.bonus}\n"
                )

            print("\nEmployee added successfully.")

        except ValueError:
            print("\nInvalid salary or bonus. Please enter numbers.")

    def read_employees(self):
        employees = []

        if not os.path.exists(self.FILE_NAME):
            return employees

        try:
            with open(self.FILE_NAME, "r") as file:

                for line in file:
                    line = line.strip()

                    if line == "":
                        continue

                    data = line.split(",")

                    employee_id = data[0]
                    name = data[1]
                    salary = float(data[2])
                    bonus = float(data[3])

                    employee = PermanentEmployee(
                        employee_id,
                        name,
                        salary,
                        bonus
                    )

                    employees.append(employee)

        except (ValueError, IndexError):
            print("Error while reading employee data.")

        return employees

    def display_all_employees(self):
        employees = self.read_employees()

        if len(employees) == 0:
            print("\nNo employees found.")
            return

        print("\n========== EMPLOYEE DETAILS ==========")

        for employee in employees:
            employee.display()
            print("--------------------------------------")

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")

        employees = self.read_employees()

        for employee in employees:

            if employee.employee_id == employee_id:
                print("\nEmployee Found!")
                employee.display()
                return

        print("\nEmployee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")

        employees = self.read_employees()

        found = False

        for employee in employees:

            if employee.employee_id == employee_id:

                found = True

                try:
                    print("\nEnter new details")

                    employee.name = input("Enter Name: ")
                    employee.salary = float(
                        input("Enter Salary: ")
                    )
                    employee.bonus = float(
                        input("Enter Bonus: ")
                    )

                except ValueError:
                    print("\nInvalid salary or bonus.")
                    return

                break

        if found:

            self.save_all_employees(employees)

            print("\nEmployee updated successfully.")

        else:
            print("\nEmployee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")

        employees = self.read_employees()

        new_employees = []

        found = False

        for employee in employees:

            if employee.employee_id == employee_id:
                found = True
            else:
                new_employees.append(employee)

        if found:

            self.save_all_employees(new_employees)

            print("\nEmployee deleted successfully.")

        else:
            print("\nEmployee not found.")

    def save_all_employees(self, employees):

        with open(self.FILE_NAME, "w") as file:

            for employee in employees:

                file.write(
                    f"{employee.employee_id},"
                    f"{employee.name},"
                    f"{employee.salary},"
                    f"{employee.bonus}\n"
                )

    def generate_salary_details(self):
        employee_id = input(
            "Enter Employee ID for salary details: "
        )

        employees = self.read_employees()

        for employee in employees:

            if employee.employee_id == employee_id:

                print("\n========== SALARY DETAILS ==========")
                print("Employee ID :", employee.employee_id)
                print("Employee Name:", employee.name)
                print("Basic Salary:", employee.salary)
                print("Bonus       :", employee.bonus)
                print("-----------------------------------")
                print(
                    "Total Salary:",
                    employee.calculate_salary()
                )
                print("===================================")

                return

        print("\nEmployee not found.")


def main():

    system = EmployeeManagementSystem()

    while True:

        print("\n")
        print("======================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Generate Salary Details")
        print("7. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_employee()

        elif choice == "2":
            system.display_all_employees()

        elif choice == "3":
            system.search_employee()

        elif choice == "4":
            system.update_employee()

        elif choice == "5":
            system.delete_employee()

        elif choice == "6":
            system.generate_salary_details()

        elif choice == "7":
            print("\nThank you for using Employee Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()