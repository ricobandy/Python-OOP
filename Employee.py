# Employee Class
class Employee:
    # class variables
    team_name = "Python"
    
    # defining the constructor for instance objects(instance variables)
    def __init__(self, id=None, salary=0, department=None):
        self.id = id
        self.salary = salary
        self.department = department

    # defining instance methods
    def tax(self):
        return self.salary * 0.2

    def salary_per_day(self):
        return self.salary / 30

    # method overloading
    def demo_one(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    # defining class methods(for accessing the class variables). All class methods have at least one argument, cls.
    @classmethod
    def get_team_name(cls):
        return cls.team_name

    # static methods are usually limited to class only and not objects
    # Have no direct relation to class varialbes or instance variables
    # used as utility inside class or when we do not want the inherited class to modify a method definition
    # Static methods can be accessed using class name or the object name
    @staticmethod
    def demo_two():
        print("This is a static method")

# Test the class by creating an object of the class
Steve = Employee()

# Print the object
print("Demo 1")
Steve.demo_one(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo_one(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo_one(1, 2, 3, 4, 5)
print("\n")

# Call the class method
print(Employee.get_team_name())

# Call static method
Steve.demo_two()
Employee.demo_two()




