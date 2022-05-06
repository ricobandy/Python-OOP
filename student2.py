class Student:
    # set private variables
    __name = None
    __rollNumber = None
    
    # defining getter and setter methods
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    # defining instance methods
