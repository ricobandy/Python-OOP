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

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    # defining class methods

# Test the class by creating an object of the class
Steve = Employee()

# Print the object
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
print("\n")



