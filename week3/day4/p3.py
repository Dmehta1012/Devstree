class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ₹{self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class Intern(Employee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

emp1 = FullTimeEmployee("Devarsh", 420, 42000)
emp2 = PartTimeEmployee("Kuldeep", 105, 30,400)
emp3 = Intern("Umesh", 103, 6000)
emp4=input("Enter your id ")
employees = [emp1, emp2, emp3,emp4]


for emp in employees:
    emp.display_info()
    