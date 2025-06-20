# Employee Class
class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Department: {self.department}")

# EMS System
class EMS:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        emp = Employee(emp_id, name, age, department)
        self.employees.append(emp)
        print("✅ Employee added successfully!\n")

    def display_all(self):
        if not self.employees:
            print("❌ No employees to display.\n")
        else:
            print("\n📋 Employee List:")
            for emp in self.employees:
                emp.display()
            print()

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("🔍 Employee Found:")
                emp.display()
                return
        print("❌ Employee not found.\n")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("✅ Employee found. Enter new details:")
                emp.name = input("Enter New Name: ")
                emp.age = int(input("Enter New Age: "))
                emp.department = input("Enter New Department: ")
                print("✅ Employee updated successfully!\n")
                return
        print("❌ Employee not found.\n")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print("🗑️ Employee deleted successfully!\n")
                return
        print("❌ Employee not found.\n")

    def run(self):
        while True:
            print("=== Employee Management System ===")
            print("1. Add Employee")
            print("2. Display All Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.display_all()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("👋 Exiting EMS. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Try again.\n")

# Run the EMS
if __name__ == "__main__":
    system = EMS()
    system.run()
