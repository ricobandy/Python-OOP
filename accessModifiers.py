class Employee:
    # defining the constructor for instance objects(instance variables)
    # all instance variables and methods are public by default
    def __init__(self, id=None, salary=0):
        self.id = id
        self.salary = salary

    # defining private instance variables
    def __init__(self, id, salary):
        self.id = id            # public instance variable                    
        self.__salary = salary # salary is a private property that is not accessible

    def display_id(self):       # public instance method
        print("ID:", self.id)

    def __display_id(self):       # private instance method accessible only within the class
        print("ID:", self.id)

    def display_salary(self):    # public instance method
        print("Salary:", self.__salary)

# Accessing private variables
Steve = Employee(100, 34764)
print(Steve._Employee__salary)