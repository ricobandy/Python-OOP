# Employee Class

class Employee:
    # defining the constructor
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # defining instance methods
    def tax(self):
        return self.salary * 0.2

    def salaryPerDay(self):
        return self.salary / 30

    # defining class methods

# Test the class by creating an object of the class
Steve = Employee(10, 5000, "customer support")
Charles = Employee()

# Print the object
print("Steve")
print("ID:", Steve.ID)
print("Salary:", Steve.salary)
print("Department:", Steve.department)
print()
print("Charles")
print("ID:", Charles.ID)
print("Salary:", Charles.salary)
print("Department:", Charles.department)




